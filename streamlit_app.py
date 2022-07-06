
import streamlit   
import pandas

streamlit.title(" My Parent's New Healthy Diner") 

streamlit.header("Breakfast Favorites")
streamlit.text("🥗 Blueberry Smoothie with Oat Milk")
streamlit.text("🥑 Avocado with Tofu Scramble")
streamlit.text("🥣 Chocolate protein Oatmeal")
streamlit.text("🍞 Bagel with Hummus")


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's put a fruit pick list here so the user can pick their own fruits
streamlit.multiselect("Pick your fruits for your smoothie!", list(my_fruit_list.index),['Avocado','Strawberry'])

#Display the table on the page
streamlit.dataframe(my_fruit_list)
