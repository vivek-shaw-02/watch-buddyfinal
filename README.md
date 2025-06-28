# 🎬 Watch Buddy 🎥 - Movie Recommendation System

![GitHub repo size](https://img.shields.io/github/repo-size/vivek-shaw-02/watch-buddyfinal)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=flat&logo=streamlit&logoColor=white)

---

## 📽️ Overview
**Watch Buddy** is a personalized movie recommendation system that suggests movies similar to your selected favorite.

✅ Powered by a **cosine similarity matrix** trained on movie metadata.  
✅ Loads a compressed model from **Google Drive on first run**, keeping the repo lightweight.  
✅ Fetches real movie posters from **OMDb API** to make your experience visual and interactive.

---

## 🚀 Features
- 🔍 **Content-based recommendations** based on genres, keywords, cast & crew
- 🎬 **Dynamic poster fetching** using OMDb API (or placeholder fallback)
- 💾 Downloads large model file dynamically from Google Drive using `gdown`
- ⚡ Built & deployed with **Streamlit**, runs in the browser
- 📝 Easily extendable for genres, ratings, or collaborative filtering

---

## 🛠 Tech Stack
- **Python 3.8+**
- **Streamlit** for UI + backend
- **pandas**, **joblib**, **gzip** for data
- **OMDb API** for poster fetching
- **Google Drive + gdown** for model storage
- **Pickle** for dataframe

---
## 📸 Screenshots

| ![Select Movie](screenshots/select_movies.PNG) |
|:--:|
| *Select a movie from the dropdown* |

| ![Recommendations](screenshots/recommendations.PNG) |
|:--:|
| *Recommended movies with posters* |


## 🚀 Quick Start

### 🔥 Clone this repo

git clone https://github.com/vivek-shaw-02/watch-buddyfinal.git
cd watch-buddyfinal
 streamlit run appp.py

🌐 Live Demo
 https://watch-buddyfinal-shjbfvd3mgps4x6ukyvxfz.streamlit.app/



## ⚙️ Project Structure

watch-buddy/
│
├── app.py
├── requirements.txt
├── movie_dict.pkl
├── similarity_compressed.pklz
├── .gitignore
└── README.md


💡 How it works
Loads your selected movie from the dropdown.

Looks up cosine similarity scores from a precomputed matrix.

Picks top 5 most similar movies.

Fetches posters via OMDb API. If unavailable, shows placeholder with movie title.

Displays them beautifully in Streamlit columns.

📝 Future Improvements
✅ Filter by genres or year
✅ Show IMDB ratings or popularity
✅ Add collaborative filtering (user-based) recommendations

## ✍️ Author
- **Vivek Shaw**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5.svg?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vivek-shaw-02)
[![GitHub](https://img.shields.io/badge/GitHub-000.svg?style=flat&logo=github&logoColor=white)](https://github.com/vivek-shaw-02)

