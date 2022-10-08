import streamlit

streamlit.title('My Moms New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥪Omega 3 & Blueberry Oatmeal')
streamlit.text('🧋Klae,Spinach & Rocket Smoothie')
streamlit.text('🍳Hard-Boiled Free-Range Egg')
streamlit.text('🥂Avacado Toast')

streamlit.header('🍉🥝Bulid Your Own Fruit Smoothie🍋🥝🍍')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
