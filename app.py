import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.title("Movie Recommendatation System")
movie_df=pickle.load(open("movie_recm.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
list_movie=np.array(movie_df["title"])
option = st.selectbox(
"Select Movie ",
(list_movie))

def show_url(movie):
     x=[]
     index = movie_df[movie_df['title'] == movie].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
     for i in distances[1:6]:

          x.append(movie_df.iloc[i[0]].urls)
     return(x)
def movie_recommend(movie):
     index = movie_df[movie_df['title'] == movie].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
     l=[]
     for i in distances[1:6]:
          l.append("{}".format(movie_df.iloc[i[0]].title))
          # return("{} {}".format(movie_df.iloc[i[0]].title, movie_df.iloc[i[0]].urls))
     return(l)
if st.button('Search'):
     st.write('Movies Recomended for you are:')
     # st.write(movie_recommend(option),show_url(option))
     df = pd.DataFrame({
          'Movie Recommended': movie_recommend(option),
          'Movie Url': show_url(option)
     })
     
     st.table(df)

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('20d96ddd.jpg')    
    