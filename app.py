from bs4 import BeautifulSoup
import requests
import streamlit as st

st.write("""
# Find out your Stock news of a Company
""")
a = st.sidebar.text_input("Enter Company name","Apple")
res = requests.get('https://www.bbc.co.uk/search?q='+a+'+stock&page=1')


soup= BeautifulSoup(res.text,'html.parser')
headline_results=soup.find_all('a',class_='css-johpve-PromoLink ett16tt7')


for news in headline_results:
    st.write(news.text)
    st.write()