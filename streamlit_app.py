import streamlit

streamlit.title('My Mom\'s new healthy diner')

streamlit.header('Breakfast Favorites')
streamlit.text(' Omega 3 & Blueberry Oatmeal')
streamlit.text(' Kale, Spinach & Rocket Smoothie')
streamlit.text(' Hard-Boiled Free-Range Egg')
streamlit.text(' Avocado Toast')

streamlit.header('Build your own fruits smoothie')

import pandas as pd

fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pick some fruits:", list(fruit_list))

streamlit.dataframe(fruit_list)
