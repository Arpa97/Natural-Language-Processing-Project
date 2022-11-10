import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval

#extract director from crew
def get_director(crew):
    for i in crew:
        if i["job"] == "Director":
            return i["name"]
    return np.nan

#return first 3 elements of input list
def get_list(x):
    if isinstance(x, list):
        names = [i["name"] for i in x]

        if len(names) > 3:
            names = names[:3]

        return names

    return []

#decapitalizes letters and removes spaces
def clean_data(row):
    if isinstance(row, list):
        return [str.lower(i.replace(" ", "")) for i in row]
    else:
        if isinstance(row, str):
            return str.lower(row.replace(" ", ""))
        else:
            return ""


def create_soup(features):
    return ' '.join(features['keywords']) + ' ' + ' '.join(features['cast']) + ' ' + features['director'] + ' ' + ' '.join(features['genres'])

def get_recommendations(title, cosine_sim, movies):
    idx = indices[title]
    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores= sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores= similarity_scores[1:11]
    # (a, b) where a is id of movie, b is similarity_scores
    movies_indices = [ind[0] for ind in similarity_scores]
    moviesT = movies["id"].iloc[movies_indices]
    return moviesT

def get_recommendation_mul(titleList, matrix, movies,) :
    vecList = []
    tls = len(titleList)

    for title in titleList :
        idx = indices[title]
        vecList.append(matrix[idx])
    meanVec = sum(vecList)/len(vecList)

    sim = cosine_similarity(meanVec, matrix)
    similarity_scores = list(enumerate(sim[0]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[tls : 10+tls]
    movies_indices = [ind[0] for ind in similarity_scores]
    moviesT = movies["id"].iloc[movies_indices]
    return moviesT

def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1


#reading csv files
if (exists("finalMovie.csv")) :
    movies = pd.read_csv("finalMovie.csv")
else :
    credits = pd.read_csv("tmdb_credits.csv")
    movies = pd.read_csv("tmdb_movies.csv")

    #merging tables
    credits.columns = ['id', 'titlec', 'cast', 'crew']
    movies = movies.merge(credits, on="id")

    #convert data to correct dataType
    columns = ["cast", "crew", "keywords", "genres"]
    for col in columns:
        movies[col] = movies[col].apply(literal_eval)

    #adding director column
    movies["director"] = movies["crew"].apply(get_director)

    #reducing cast, keywords and genres to max 3 elements
    columns = ["cast", "keywords", "genres"]
    for col in columns:
        movies[col] = movies[col].apply(get_list)

    #format datas
    columns = ['cast', 'keywords', 'director', 'genres']
    for col in columns:
        movies[col] = movies[col].apply(clean_data)

    #create soup
    movies["soup"] = movies.apply(create_soup, axis=1)
    movies.to_csv('finalMovie.csv', index = False)

#vectorize soup (count method) calculate similarity
count_vectorizer = CountVectorizer(stop_words="english")
count_matrix = count_vectorizer.fit_transform(movies["soup"])
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

#vactorize overview whit tfidf
tfidf = TfidfVectorizer(stop_words="english")
movies["overview"] = movies["overview"].fillna("")
tfidf_matrix = tfidf.fit_transform(movies["overview"])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


#reset movie indices, map film title to indices
movies = movies.reset_index()
indices = pd.Series(movies.index, index=movies["title"])
indices = pd.Series(movies.index, index=movies["title"]).drop_duplicates()

#DEV TESTS FOR ALGORITHMS

#print("################ Content Based System - metadata #############")
#print("Recommendations for The Dark Knight Rises")
#print(get_recommendations("The Dark Knight Rises", cosine_sim2, movies))
#print()
#print("Recommendations for Avengers")
#print(get_recommendations("The Avengers", cosine_sim2, movies))

#print("################ Content Based Filtering - plot#############")
#print()
#print("Recommendations for The Dark Knight Rises")
#print(get_recommendations("The Dark Knight Rises", cosine_sim, movies))
#print()
#print("Recommendations for Avengers")
#print(get_recommendations("The Avengers", cosine_sim, movies))

#titleList = ["The Dark Knight Rises", "The Avengers"]

#print("################ Content Based Filtering - metadata #############")
#print()
#print("Recommendations for The Dark Knight Rises and avengers")
#print(get_recommendation_mul(titleList, count_matrix, movies))
#print("################ Content Based Filtering - plot #############")
#print()
#print("Recommendations for The Dark Knight Rises and avengers")
#print(get_recommendation_mul(titleList, tfidf_matrix, movies))

#--------USER INTERFACE-----#
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def fetch_title(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    title = data['title']
    return title

def recommend(movie):
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended = get_recommendations(movie, cosine_sim, movies);
    for i in range(0, 10):
        recommended_movie_posters.append(fetch_poster(recommended.iloc[i]))
        recommended_movie_names.append(fetch_title(recommended.iloc[i]))

    return recommended_movie_names,recommended_movie_posters

def recommend2(movie):
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended = get_recommendations(movie, cosine_sim2, movies);
    for i in range(0, 10):
        recommended_movie_posters.append(fetch_poster(recommended.iloc[i]))
        recommended_movie_names.append(fetch_title(recommended.iloc[i]))

    return recommended_movie_names,recommended_movie_posters

def recommend3(movieLis):
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended = get_recommendation_mul(movieLis, tfidf_matrix, movies);
    for i in range(0, 10):
        recommended_movie_posters.append(fetch_poster(recommended.iloc[i]))
        recommended_movie_names.append(fetch_title(recommended.iloc[i]))

    return recommended_movie_names,recommended_movie_posters

def recommend4(movieLis):
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended = get_recommendation_mul(movieLis, count_matrix, movies);
    for i in range(0, 10):
        recommended_movie_posters.append(fetch_poster(recommended.iloc[i]))
        recommended_movie_names.append(fetch_title(recommended.iloc[i]))

    return recommended_movie_names,recommended_movie_posters


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation Based on Plot'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

if st.button('Show Metadata Based Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend2(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])


selected_movies = st.multiselect(
    "Type movies you like",
    movie_list
)

if st.button('Show Recommendation Based on Plot Taste'):
    recommended_movie_names,recommended_movie_posters = recommend3(selected_movies)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

if st.button('Show Recommendation Based on Meta Taste'):
    recommended_movie_names,recommended_movie_posters = recommend3(selected_movies)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
