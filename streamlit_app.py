import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_to_show = my_fruit_list.loc[my_fruit_list]

# Let's put a pick list here so they can pick the fruit  they want to include
##streamlit.multiselect("Pick some fruits", list(my_fruit_list.index),['Avocado','Strawberries'])

#display table on the page
streamlit.dataframe(fruits_to_show)
