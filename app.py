import streamlit as st
import pickle
import pandas as pd

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation logic
def recommend(movie):
    movie = movie.lower()
    if movie not in movies['title'].str.lower().values:
        return []
    index = movies[movies['title'].str.lower() == movie].index[0]
    distances = list(enumerate(similarity[index]))
    movie_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
    return [movies.iloc[i[0]].title for i in movie_list]

# Page configuration
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

# --- Custom CSS ---
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .container {
        padding: 2rem;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        max-width: 700px;
        margin: auto;
    }
    h1 {
        text-align: center;
        color: #333333;
        margin-bottom: 2rem;
    }
    .movie-card {
        background-color: #fafafa;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        font-size: 17px;
        font-weight: 500;
        color: #333;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Main App ---
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<h1>🎥 Movie Recommender</h1>', unsafe_allow_html=True)

selected_movie = st.selectbox("🎞️ Choose a movie you like:", movies['title'].values)

if st.button("Get Recommendations"):
    recommendations = recommend(selected_movie)
    if recommendations:
        st.subheader("✨ Recommended for You:")
        for movie in recommendations:
            st.markdown(f'<div class="movie-card">👉 {movie}</div>', unsafe_allow_html=True)
    else:
        st.warning("Sorry, movie not found!")

st.markdown("</div>", unsafe_allow_html=True)
