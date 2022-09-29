import pandas as pd
import streamlit as st


st.sidebar.text('')
st.sidebar.text('')
st.sidebar.text('')
st.sidebar.markdown("""# Table of contents
- ### [Home](#insight-hasil-tani-indonesia)
- ### [Total Hasil tani dari tahun 2000 hingga 2021](#total-hasil-tani-dari-tahun-2000-hingga-2021)
- ### [Data Tahunan hasil tani](#data-tahunan-hasil-tani)
- ### [Jenis hasil tani terbanyak dari tahun 2000 hingga 2021](#jenis-hasil-tani-terbanyak-dari-tahun-2000-hingga-2021)
                      """)


st.write("# Insight Hasil Tani Indonesia")

top_provinsi = pd.read_csv('dataset/top_provinsi_2000-2021.csv')

st.write('## Total Hasil tani dari tahun 2000 hingga 2021')
st.bar_chart(top_provinsi,y='total',x='provinsi',height=600)
if st.checkbox('Show dataframe'):
    top_provinsi

top_anual_value = pd.read_csv('dataset/anual_value.csv')

st.write('## Data Tahunan hasil tani')
st.bar_chart(top_anual_value,y='total',x='date',height=600)
if st.checkbox('Show dataframe_'):
    top_anual_value

top_commodity = pd.read_csv('dataset/top_commodity.csv')

st.write('## Jenis hasil tani terbanyak dari tahun 2000 hingga 2021')
st.bar_chart(top_commodity,y='total',x='jenis_tani',height=450)
if st.checkbox('Show dataframe#'):
    top_commodity

top_commodity = pd.read_csv('dataset/top_commodity.csv')

st.write('## Jenis hasil tani terbanyak dari tahun 2000 hingga 2021')
st.bar_chart(top_commodity,y='total',x='jenis_tani',height=450)
if st.checkbox('Show dataframe#'):
    top_commodity

import streamlit as st
import plotly.figure_factory as ff
import numpy as np

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

