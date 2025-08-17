# ML-DL-project-CDAC-DBDA
# 🛍️ AI Generated E-commerce Product Review Summarization

## 🌐 Live Demo
Access the deployed app here: **[[Link to Streamlit App on AWS](http://13.233.216.37:8501)]**

## 📌 Overview
This project is inspired by Amazon’s AI product review summaries and aims to **automatically generate concise, informative summaries** from raw customer reviews scraped from **Flipkart**.  
It combines **data scraping**, **intelligent preprocessing**, **Transfer Learning**, and **interactive deployment** to deliver real-time product insights.

---

## 🚀 Features
- **Automated Review Scraping** – Uses Selenium to scrape 60K+ reviews from Flipkart.  
- **Smart Data Cleaning** – Removes emojis, non-English reviews, duplicates, and noise while preserving meaning.  
- **Dynamic Token-based Chunking** – Prevents model truncation for long inputs while keeping semantic context intact.  
- **AI-powered Summarization** – Utilizes Google Gemini API for pseudo-label generation, then fine-tunes **Facebook’s BART model** for domain-specific summarization.  
- **Interactive Web App** – Built with Streamlit for on-demand summarization of any Flipkart product.  
- **AWS EC2 Deployment** – Accessible online so anyone with the link can use the app.

---

## 🛠️ Tech Stack
- **Web Scraping:** Selenium  
- **Data Processing:** Python, Regex, LangDetect  
- **Model Training:** Hugging Face Transformers, Facebook BART
- **Pseudo-labeling:** Google Gemini API  
- **Frontend:** Streamlit  
- **Deployment:** AWS EC2  

---
---

## 💻 How It Works
1. **Scrape Reviews** – Fetches reviews for a given product directly from Flipkart.  
2. **Preprocess** – Cleans and filters reviews (English only, no duplicates, min length).  
3. **Chunk Long Texts** – Splits aggregated reviews into token-friendly chunks.  
4. **Summarize** – Generates summaries using a fine-tuned BART model.  
5. **Deploy** – Hosts the interactive app on AWS EC2.

---

---

## 🌐 Live Demo
Access the deployed app here: **[[Link to Streamlit App on AWS](http://13.233.216.37:8501)]**

---

## 📜 License
This project is licensed under the MIT License.
