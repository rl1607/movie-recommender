import streamlit as st
import pickle
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------- Load Data FIRST ----------
movies = pickle.load(open('movies.pkl', 'rb'))

# ---------- Compute Similarity AFTER loading ----------
@st.cache_resource
def compute_similarity(data):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(data['tags']).toarray()
    return cosine_similarity(vectors)

similarity = compute_similarity(movies)

# ---------- Load Data ----------
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ---------- Session State ----------
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

# 🔑 OMDb API Key (replace with your key)
API_KEY = "727fb434"

# ---------- Fetch Poster ----------
def fetch_poster(movie_title):
    try:
        url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
        data = requests.get(url).json()

        if data.get("Response") == "True":
            poster = data.get("Poster")
            if poster and poster != "N/A":
                return poster

        return "https://via.placeholder.com/300x450?text=No+Image"
    except:
        return "https://via.placeholder.com/300x450?text=Error"

# ---------- Recommend ----------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []

    for i in movies_list:
        title = movies.iloc[i[0]].title
        names.append(title)
        posters.append(fetch_poster(title))

    return names, posters

# ---------- Smart Search ----------
def search_movies(query):
    query = query.lower()

    results = movies[
        movies['title'].str.lower().str.contains(query, na=False) |
        movies['tags'].str.lower().str.contains(query, na=False)
    ]

    return results['title'].values[:10]

# ---------- UI ----------
st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommender System")
st.markdown("### 🔍 Search Movie (name or keyword)")

search_query = st.text_input("Type movie name...")

# ---------- Search Results ----------
if search_query:
    results = search_movies(search_query)

    if len(results) > 0:
        st.markdown("### 🎬 Matching Movies")

        for idx, movie in enumerate(results):
            if st.button(movie, key=f"btn_{idx}"):
                st.session_state.selected_movie = movie
    else:
        st.warning("No movies found")

# ---------- Selected Movie + Recommendations ----------
if st.session_state.selected_movie:

    selected = st.session_state.selected_movie

    st.markdown("## 🎬 Selected Movie")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(fetch_poster(selected), width=200)

    with col2:
        st.subheader(selected)

    st.markdown("## 🎯 Recommended Movies")

    names, posters = recommend(selected)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.image(posters[i], width=150)
            st.caption(names[i])