
from transformers import BartForConditionalGeneration, BartTokenizer
import torch
import random
from pathlib import Path
# import json

from prediction_reviews_cleaning import clean_text, preprocess_reviews
from scrapping_script import scrape_review

# Path to the directory where your model was saved
model_dir = r".\tuned_model_files"  # change if your output_dir is different

# Load tokenizer & model
tokenizer = BartTokenizer.from_pretrained(model_dir)
model = BartForConditionalGeneration.from_pretrained(model_dir)
#----
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)
#---

#==========

#chunking and combining the reviews
def block_reviews(reviews, max_words=900):
    chunks = []
    current_chunk = []
    current_word_count = 0

    for review in reviews:
        review_word_count = len(tokenizer.encode(review.split(), add_special_tokens=False)) #Limits by token count instead of word count (useful for transformers)

        # Check if adding this review would exceed max_words
        if current_word_count + review_word_count > max_words:
            # Finalize current chunk and start a new one
            chunks.append(" ".join(current_chunk))
            current_chunk = [review]
            current_word_count = review_word_count
        else:
            current_chunk.append(review)
            current_word_count += review_word_count

    # Add the last chunk (if any reviews left)
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def chunk_and_summarize(combined_reviews):
    # Split into chunks

    summaries = []   
    random.shuffle(combined_reviews) # so that the order of chunks/batch of reviews is mixed
    
    for batch in combined_reviews:
        inputs = tokenizer(batch, return_tensors="pt", max_length=1024, truncation=True, padding=True)
        inputs = {key: val.to(device) for key, val in inputs.items()}
        # inputs = inputs.to(device)
        summary_ids = model.generate(input_ids=inputs['input_ids'],
            attention_mask=inputs['attention_mask'], max_length=100, min_length=20, length_penalty=1.0, num_beams=6,early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary)
    
    # Combine and summarize again if needed
    combined_summary = " ".join(summaries)
    if len(combined_summary.split()) > 200:
        # Final summarization pass
        final_inputs = tokenizer(combined_summary, return_tensors="pt", max_length=1024, truncation=True, padding=True )
        final_inputs = {key: val.to(device) for key, val in final_inputs.items()}
        # final_inputs=final_inputs.to(device)

        final_summary = model.generate( input_ids=final_inputs['input_ids'],
            attention_mask=final_inputs['attention_mask'], max_length=200, min_length=80,length_penalty=2.0, num_beams=7,early_stopping=True)
        torch.cuda.empty_cache()
        return tokenizer.decode(final_summary[0], skip_special_tokens=True) 
    torch.cuda.empty_cache()
    return combined_summary
    

#============================================================
#============================================================


product_query="Redmi note 4"
#(here the name(string) of the product entered by user in app should come)
#-----------------------------------------
# 1)HERE THE SELENIUM/BEAUTIFUL_S WILL TAKE THIS "PRODUCT_QUERY" AS INPUT
# 2) THE OUTPUT(WE'LL LIMIT TO 200 REVIEWS(RAW) WILL BE A JSON FILE)
# 3) WE WILL DIRECTLY PASS THAT FILE TO CLEANING CODE
# 4) FROM THERE THERE(THE BASE CODE) WILL CAPTURE IT
#-----------------------------------------


scrapped_data= scrape_review(product_query)

cleaned_data=preprocess_reviews(scrapped_data)


# Extract and filter cleaned comments with word count >= 6
cleaned_reviews= [
    review.get("cleaned_comment","")
    for review in cleaned_data["cleaned_reviews"]
]

#============================================================
#============================================================

list_of_combined_reviews_by_block=block_reviews(cleaned_reviews)
final_summary = chunk_and_summarize(list_of_combined_reviews_by_block)
print(f"THE FINAL SUMMARY FOR THE PRODUCT {product_query}:- {final_summary}")
# >>>This final summary is to be printed on the app page

#============================================================
#============================================================
#==========









# # directory where where the cleaned review
# base_dir = Path(r"d:\CDAC\1. PG DBDA\project cdac\Data Cleaning\Only_cleaned_reviews")
# # brand_folder = base_dir / brand
# # pattern = f"{selected_brand} {model}_flipkart_proper_reviews.json"
# pattern = f"{product_query}_flipkart_proper_reviews.json"

# path= base_dir / pattern

# # Your JSON data 
# # Open and load the JSON file
# with open(path, 'r', encoding='utf-8') as file:
#     data = json.load(file)

# Extract the search query
# Product_name = cleaned_data["product"]
