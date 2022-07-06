
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
streamlit.dataframe(my_fruit_list)
