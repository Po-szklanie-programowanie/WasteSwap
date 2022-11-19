import streamlit as st
import pandas 
import plotly.express
import streamlit.components.v1 as components

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.title('WasteSwap')

szukanie = st.text_input('wpisz produkt którego pragniesz')
