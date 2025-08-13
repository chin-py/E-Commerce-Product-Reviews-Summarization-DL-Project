

import re
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
# import glob
# import os
# import nltk
# from nltk.corpus import words
# import string

# def filter_known_words(text):
#     words_list = text.split()
#     english_words = [word for word in words_list if word.lower() in english_vocab]
#     return ' '.join(english_words)

def clean_text(text):
    # Remove emojis
    text = re.sub(r'[^\w\s.,!?\'\":;%()&-]', '', text)
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    # Remove unwanted char sequences
    text = re.sub(r"\s\b\w*\s?\.{3,}\s*\n?READ MORE", '.', text) # \s space,\b word boundry,\w* any number of word characters, ? for optional presence.\n newline char,{3,} 3 or more of prev char
    # Remove unwanted char sequences
    text = re.sub(r'\.{2,}', '. ', text)
    # Remove extra spaces and newlines
    text = re.sub(r'\s+', ' ', text).strip()


    # Remove unwanted char sequences
    text = re.sub(r'\.READ MORE', '. ', text).strip()
    # Remove unwanted char sequences
    text = re.sub(r'\.{2,}', '. ', text)


    # Remove non-English words
    # nltk.download('words')
    # english_vocab = set(words.words())
    # cleaned_title = filter_known_words(text)

    # Convert to lowercase
    return text.lower()


###############################################################
def preprocess_reviews(data):
    # overall_rating = None
    # total_ratings_cleaned = "0"
    # Clean fields
    if "Overall_rating" in data:
        try:
            overall_rating = float(data.get("Overall_rating", 0))
        except ValueError:
            overall_rating = None  # No valid rating found
    
    if "Total_ratings" in data:
        try:
            total_ratings_raw = data.get("Total_ratings", "").replace(" Ratings &", "").strip()
            total_ratings_cleaned = int(total_ratings_raw.replace(",", ""))
        except ValueError:
             total_ratings_cleaned = 0  # No valid count found
   
   
    new_data = {
    "product": data["search_query"],
    "total_initial_review_count": data["total_reviews"],
    "total_final_review_count": 0,
    "overall_rating": overall_rating,
    "total_ratings_count": total_ratings_cleaned,
    "cleaned_reviews": []
    }


    # Determine min word count based on total_reviews
    min_words = 15 if data["total_reviews"] >= 100 else 10

    # Process each review
    for review in data.get("reviews", []):
        cleaned_title = clean_text(review.get("Title", ""))

        try:
            if detect(review.get("Comment", "")) != 'en':  # check if review not in english
                continue
        except LangDetectException:
             continue  # Skip  (The langdetect.detect() function fails if the input is empty,too short, or contains no detectable language — e.g., just emojis, short string like "ok".)
        
        cleaned_comment = clean_text(review.get("Comment", ""))

        # Check word count and append if within bounds
        word_count = len(cleaned_comment.split())
        if min_words < word_count:   # Skip if too short
            new_data["cleaned_reviews"].append({
                "title": cleaned_title,
                "raw_comment":review.get("Comment",""),
                "cleaned_comment": cleaned_comment

            })

#####
# The difference between review["comment"] and review.get("comment", "") when accessing data from a JSON-like dictionary in Python is primarily in error handling and default value behavior.
# Safe Access: Returns the value for "comment" if it exists, otherwise returns the default value "".
# Prevents KeyError: If the key "comment" is missing from the dictionary, it won’t raise an exception.
# Customizable default: You can choose any default value (e.g., None, "N/A", etc.).

    new_data["total_final_review_count"]=len(new_data["cleaned_reviews"])

    return new_data


####################################################
# here the input is the output of selenium code

# data_with_cleaned_reviews = preprocess_reviews(data)

# output_file = os.path.join(output_dir, f"{base_name}_proper_reviews.json")
# # Optional: Save cleaned data
# with open(output_file, "w", encoding='utf-8') as f:
#     json.dump(data_with_cleaned_reviews, f, ensure_ascii=False, indent=2)