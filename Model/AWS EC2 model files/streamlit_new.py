import streamlit as st
from transformers import BartForConditionalGeneration, BartTokenizer
import torch
import random
from pathlib import Path
import time

# Import your existing modules
from prediction_reviews_cleaning import clean_text, preprocess_reviews
from scrapping_new import scrape_review

# Set page configuration
st.set_page_config(
    page_title="Product Review Summarizer",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"

)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .product-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .summary-card {
        background-color: #e8f4fd;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    .metric-card {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #ffeaa7;
        text-align: center;
        margin: 0.5rem;
    }
    .stButton > button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        border: none;
        padding: 0.75rem;
        border-radius: 5px;
        font-size: 1.1rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'model_loaded' not in st.session_state:
    st.session_state.model_loaded = False
if 'model' not in st.session_state:
    st.session_state.model = None
if 'tokenizer' not in st.session_state:
    st.session_state.tokenizer = None

@st.cache_resource
def load_model():
    """Load the fine-tuned BART model and tokenizer"""
    try:
        model_dir = "./tuned_model_files"
        tokenizer = BartTokenizer.from_pretrained(model_dir)
        model = BartForConditionalGeneration.from_pretrained(model_dir)
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model.to(device)
        return model, tokenizer, device
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None, None, None

def block_reviews(reviews, tokenizer, max_words=900):
    """Chunk reviews into manageable blocks"""
    chunks = []
    current_chunk = []
    current_word_count = 0

    for review in reviews:
        review_word_count = len(tokenizer.encode(review.split(), add_special_tokens=False))

        if current_word_count + review_word_count > max_words:
            chunks.append(" ".join(current_chunk))
            current_chunk = [review]
            current_word_count = review_word_count
        else:
            current_chunk.append(review)
            current_word_count += review_word_count

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def chunk_and_summarize(combined_reviews, model, tokenizer, device):
    """Generate summaries from chunked reviews"""
    summaries = []   
    random.shuffle(combined_reviews)
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, batch in enumerate(combined_reviews):
        status_text.text(f"Processing chunk {i+1} of {len(combined_reviews)}...")
        progress_bar.progress((i + 1) / len(combined_reviews))
        
        inputs = tokenizer(batch, return_tensors="pt", max_length=1024, truncation=True, padding=True)
        inputs = {key: val.to(device) for key, val in inputs.items()}
        
        with torch.no_grad():
            summary_ids = model.generate(
                input_ids=inputs['input_ids'],
                attention_mask=inputs['attention_mask'], 
                max_new_tokens=150, 
                min_length=70, 
                length_penalty=1.0, 
                num_beams=6,
                eos_token_id=tokenizer.eos_token_id,
                early_stopping=True
            )
        
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary)
    
    # Combine and summarize again if needed
    combined_summary = " ".join(summaries)
    
    if len(combined_summary.split()) > 250:
        status_text.text("Generating final summary...")
        final_inputs = tokenizer(combined_summary, return_tensors="pt", max_length=1024, truncation=True, padding=True)
        final_inputs = {key: val.to(device) for key, val in final_inputs.items()}

        with torch.no_grad():
            final_summary = model.generate(
                input_ids=final_inputs['input_ids'],
                attention_mask=final_inputs['attention_mask'], 
                max_new_tokens=250, 
                min_length=100,
                length_penalty=1.5, 
                num_beams=7,
                eos_token_id=tokenizer.eos_token_id,
                early_stopping=True
            )
        
        final_result = tokenizer.decode(final_summary[0], skip_special_tokens=True)
    else:
        final_result = combined_summary
    
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    
    progress_bar.empty()
    status_text.empty()
    
    return final_result

# Main app
def main():
    # Header
    st.markdown('<h1 class="main-header">🛍️ Product Review Summarizer</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("📊 App Information")
        st.info("Get real-time, AI generated reviews' summary for any product on Flikart🛒 powered fine-tuned BART model on primary data scrapped using selenium from the same Flipkart.")
        
        st.header("⚙️ Model Status")
        if not st.session_state.model_loaded:
            if st.button("🔄 Load Model"):
                with st.spinner("Loading model..."):
                    model, tokenizer, device = load_model()
                    if model is not None:
                        st.session_state.model = model
                        st.session_state.tokenizer = tokenizer
                        st.session_state.device = device
                        st.session_state.model_loaded = True
                        st.success("✅ Model loaded successfully!")
                        st.rerun()
                    else:
                        st.error("❌ Failed to load model")
        else:
            st.success("✅ Model is loaded and ready!")
    
    # Main content
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### Enter Product Name")
        product_query = st.text_input(
            "",
            placeholder="e.g., iPhone 15, Samsung Galaxy S24...",
            help="Enter product name you want to analyze reviews for"
        )
        
        analyze_button = st.button("🔍 Analyze Reviews", disabled=not st.session_state.model_loaded)
    
    if analyze_button and product_query:
        if not st.session_state.model_loaded:
            st.error("Please load the model first from the sidebar!")
            return
            
        try:
            # Step 1: Scrape reviews
            with st.spinner("🔍 Scraping reviews..."):
                scrapped_data = scrape_review(product_query)
            
            # if not scrapped_data or not scrapped_data.get("reviews"):
            #     st.error("No reviews found for this product. Please try a different product name.")
            #     return
            if not scrapped_data:
                st.error("Scraping failed. Check logs or try again.")
                return
            
            # Step 2: Clean and preprocess
            with st.spinner("🧹 Cleaning and preprocessing reviews..."):
                cleaned_data = preprocess_reviews(scrapped_data)
            
            # Extract cleaned reviews
            cleaned_reviews = [
                review.get("cleaned_comment", "")
                for review in cleaned_data["cleaned_reviews"]
                if review.get("cleaned_comment", "").strip()  # Only non-empty reviews
            ]
            
            if not cleaned_data.get("cleaned_reviews"):
                st.error("No valid reviews found after cleaning. Please try a different product.")
                return
            
            # Display product information
            st.markdown("---")
            st.markdown("## 📱 Product Information")
            
            # Product details card
            st.markdown(f'''
            <div class="product-card" style="background-color: black; color: white; padding: 10px; border-radius: 8px; text-align: center;">
                <h3>🎯 {cleaned_data.get("product", "Unknown Product")}</h3>
            </div>
            ''', unsafe_allow_html=True)
            
            # Metrics
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.metric(
                    "⭐ Overall Rating",
                    f"{cleaned_data.get('overall_rating', 'N/A')}",
                    help="Average rating of the product"
                )
                st.markdown("</div>", unsafe_allow_html=True)
            
            with col2:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.metric(
                    "📊 Total Ratings",
                    f"{cleaned_data.get('total_ratings_count', 'N/A'):,}",
                    help="Total number of ratings"
                )
                st.markdown("</div>", unsafe_allow_html=True)
            
            with col3:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.metric(
                    "📝 Initial Reviews",
                    f"{cleaned_data.get('total_initial_review_count', 'N/A')}",
                    help="Number of reviews scraped"
                )
                st.markdown("</div>", unsafe_allow_html=True)
            
            # with col4:
            #     st.metric(
            #         "✅ Final Reviews",
            #         f"{cleaned_data.get('total_final_review_count', len(cleaned_reviews))}",
            #         help="Number of reviews after cleaning"
                
            
            # Step 3: Generate summary
            with st.spinner("🤖 Generating AI summary..."):
                list_of_combined_reviews_by_block = block_reviews(
                    cleaned_reviews, 
                    st.session_state.tokenizer
                )
                
                final_summary = chunk_and_summarize(
                    list_of_combined_reviews_by_block,
                    st.session_state.model,
                    st.session_state.tokenizer,
                    st.session_state.device
                )
            
            # Display summary
            # st.markdown("---")
            # st.markdown("## 📋 AI-Generated Summary")
            
            # st.markdown(f'''
            # <div class="summary-card">
            #     <h4>🎯 Review Summary</h4>
            #     <p style="font-size: 1.1rem;background-color: black; color: white; line-height: 1.6; margin-top: 1rem;">
            #         {final_summary}
            #     </p>
            # </div>
            # ''', unsafe_allow_html=True)
            st.markdown("---")
            st.markdown(
                f"""
                <div class="summary-card" style="background-color: black; color: white; padding: 15px; border-radius: 8px;">
                    <h2>📋 AI-Generated Summary</h2>
                    <h4>🎯 Review Summary</h4>
                    <p style="font-size: 1.1rem; line-height: 1.6; margin-top: 1rem;">
                        {final_summary}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

            
            
            # Additional information
            with st.expander("📊 View Additional Details"):
                st.json({
                    "product": cleaned_data.get("product", "Unknown"),
                    "total_initial_review_count": cleaned_data.get("total_initial_review_count", 0),
                    # "total_final_review_count": cleaned_data.get("total_final_review_count", len(cleaned_reviews)),
                    "overall_rating": cleaned_data.get("overall_rating", 0),
                    "total_ratings_count": cleaned_data.get("total_ratings_count", 0),
                    "summary_length": len(final_summary.split()),
                    "chunks_processed": len(list_of_combined_reviews_by_block)
                })
                
            st.success("✅ Analysis completed successfully!")
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("Please check your internet connection and try again.")

if __name__ == "__main__":
    main()