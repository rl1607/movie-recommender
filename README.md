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

##snapshots
<img width="1920" height="1014" alt="Screenshot (116)" src="https://github.com/user-attachments/assets/67cc1b72-e0d2-4aeb-ad75-f5ccb9a40e7c" />
<img width="1920" height="1008" alt="Screenshot (117)" src="https://github.com/user-attachments/assets/71fecd35-10bb-450d-9b21-e941fd2c5399" />
<img width="1920" height="1021" alt="Screenshot (118)" src="https://github.com/user-attachments/assets/a9fd0d2e-7ed7-4126-b4c9-45974bca03ca" />
<img width="1920" height="1014" alt="Screenshot (119)" src="https://github.com/user-attachments/assets/e6c6f7d7-3bb9-4741-a5e0-5677d1c73592" />




