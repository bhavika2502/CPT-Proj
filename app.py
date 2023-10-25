import streamlit as st
import requests 
import pandas as pd

def recommend(movie):
    movie_name = input('Enter your favourite movie name: ')
    list_of_all_titles = movies_data['title'].tolist()
    find_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    close_match = find_match[0]
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
    print('Movies suggested for you: \n')
    i = 1
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_data[movies_data.index==index]['title'].values[0]
        if (i<10):
            print(i, '.', title_from_index)
            i+=1


st.header("Movie Recommendation System using ML")

movies= pd.read_csv('Back-end\Data\movies.csv')


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie to get recommendation",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movies_name = recommend(seleceted_movie)


    
