# movie-recommender
A content-based movie recommendation system built using Python, Machine Learning, and Streamlit. Recommends similar movies based on genres,  keywords, and overview with an interactive search UI.

## 📌 Overview
This project is a content-based movie recommendation system that suggests similar movies based on their features such as genres, cast, keywords, and overview.

## 🚀 Features
- 🔍 Smart search (name + keyword)
- 🎯 Recommends top 5 similar movies
- 🎬 Displays movie posters
- ⚡ Interactive UI using Streamlit

## 🧠 How It Works
- Data is taken from the TMDB 5000 movie dataset
- Important features like genres, cast, and overview are combined into a single column
- Text data is converted into numerical vectors using CountVectorizer
- Cosine similarity is used to find similar movies

## 🛠 Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit
- Requests (for poster API)

## ▶️ Run Locally
```bash
pip install -r requirements.txt
python -m streamlit run app.py
