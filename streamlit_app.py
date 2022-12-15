import streamlit
import pandas as pd

streamlit.title("My parents healthy diner !!")
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

item_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
item_list = item_list.set_index('Fruit')

streamlit.dataframe(item_list.index)

streamlit.multiselect("Pick some fruits:", list(item_list.index))
streamlit.dataframe(item_list)


