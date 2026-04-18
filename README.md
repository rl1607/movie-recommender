# 🎬 Movie Recommender System

## 📌 Overview
This is a content-based movie recommendation system that suggests similar movies based on features like genres, cast, keywords, and overview.

---

## 🌐 Live Demo
🚀 Try the app here:  
https://movie-recommender-3xhhayebnjuccahmdmqit6.streamlit.app/

---

## 🚀 Features
- 🔍 Smart search (by movie name or keyword)
- 🎯 Recommends top 5 similar movies
- 🎬 Displays movie posters
- ⚡ Interactive UI using Streamlit
- 🧠 Content-based filtering using ML

---

## 🧠 How It Works
- Data is taken from the TMDB 5000 movie dataset
- Important features like genres, cast, and overview are combined into a single column (`tags`)
- Text is converted into numerical vectors using **CountVectorizer**
- **Cosine similarity** is used to find similar movies

---

## 🛠 Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit
- Requests (OMDb API)

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
