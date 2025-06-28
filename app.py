import streamlit as st
import pickle
import pandas as pd
import requests
import os
import gdown
import joblib
import gzip

# Download similarity file if needed
if not os.path.exists("similarity_compressed.pklz"):
    print("Downloading similarity_compressed.pklz from Google Drive...")
    url = "https://drive.google.com/uc?id=1zfNUrPj18thQUm-t-vttC_Ta8dVa0tw_"
    gdown.download(url, "similarity_compressed.pklz", quiet=False)

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

with gzip.open('similarity_compressed.pklz', 'rb') as f:
    similarity = joblib.load(f)

# Robust poster fetcher
def fetch_poster(movie_name):
    try:
        url = f"http://www.omdbapi.com/?t={movie_name}&apikey=fd22ff34"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_url = data.get('Poster')
        if poster_url and poster_url != "N/A":
            return poster_url
        else:
            return f"https://via.placeholder.com/300x450.png?text={movie_name.replace(' ', '+')}"
    except Exception as e:
        print(f"Poster error for {movie_name}: {e}")
        return f"https://via.placeholder.com/300x450.png?text={movie_name.replace(' ', '+')}"


# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_name = movies.iloc[i[0]].title
        recommended_movies.append(movie_name)
        recommended_movies_posters.append(fetch_poster(movie_name))
    return recommended_movies, recommended_movies_posters

# Streamlit UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])

