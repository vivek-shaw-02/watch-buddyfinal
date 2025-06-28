import streamlit as st
import pickle
import pandas as pd
import requests
import os
import gdown

if not os.path.exists("similarity_compressed.pklz"):
    print("Downloading similarity_compressed.pklz from Google Drive...")
    url = "https://drive.google.com/uc?id=1zfNUrPj18thQUm-t-vttC_Ta8dVa0tw_"
    gdown.download(url, "similarity_compressed.pklz", quiet=False)



# Fetch poster with safe API call

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except requests.exceptions.Timeout:
        print(f"Timeout fetching movie {movie_id}")
        return "https://via.placeholder.com/500?text=Timeout"
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        return "https://via.placeholder.com/500?text=HTTPError"
    except Exception as e:
        print(f"Other error: {e}")
        return "https://via.placeholder.com/500?text=Error"


# Recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


# Load data

import joblib
import gzip

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

with gzip.open('similarity_compressed.pklz', 'rb') as f:
    similarity = joblib.load(f)


# Streamlit UI

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
