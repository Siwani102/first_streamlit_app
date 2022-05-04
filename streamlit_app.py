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

fruit_selected = streamlit.multiselect("Pick some fruits:", list(fruit_list.index))

streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice') 
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests

fruits_to_show = fruit_list.loc[fruit_selected]
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")

fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)


import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from frut_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("HThe fruit load list contains:")
streamlit.text(my_data_row)
