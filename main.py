import pandas as pd
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import preprocessing,feature_selection
import json

#! this is side bar
st.sidebar.text('')
st.sidebar.text('')
st.sidebar.text('')
st.sidebar.markdown("""# Table of contents
- ### [Home](#insight-hasil-tani-indonesia)
- ### [Total Hasil tani dari tahun 2000 hingga 2021](#total-hasil-tani-dari-tahun-2000-hingga-2021)
- ### [Data Tahunan hasil tani](#data-tahunan-hasil-tani)
- ### [Jenis hasil tani terbanyak dari tahun 2000 hingga 2021](#jenis-hasil-tani-terbanyak-dari-tahun-2000-hingga-2021)
                      """)

#! this is title
st.write("# Data hasil produksi tani dan pemanasan global Indonesia")
st.write('Pemanasan global adalah kejadian meningkatnya temperatur rata-rata atmosfer,laut dan daratan Bumi. Permasalahan yang dihadapi saat ini adalah meningkatnya suhu global diperkirakan akan menyebabkan perubahan-perubahan yang lain seperti naiknya permukaan air laut, meningkatnya intensitas fenomena cuaca yang ekstrim, Akibat-akibat dari meningkatnya suhu global diantaranya adalah terpengaruhnya hasil pertanian.')

#! hasil tani 2000 - 2021
top_provinsi = pd.read_csv('dataset/top_provinsi_2000-2021.csv')
st.write('## Total produksi tani seluruh provinsi dari tahun 2000 hingga 2021 ')
st.write('Data dibawah ini adalah total hasil produksi 25 jenis pertanian yang telah di kelompokan berdasarkan provinsinya. 25 jenis pertanian itu adalah Bawang Merah, Bawang Putih, Bawang Daun, Kentang, Kubis, Kembang Kol, Petsai/Sawi, Wortel, Lobak, Kacang Merah, Kacang Panjang, Cabai Besar, Cabai Rawit, Tomat, Terung, Buncis, Ketimun, Labu Siam, Kangkung, Bayam, Melinjo, Paprika, Jamur, Petai dan Jengkol')
st.bar_chart(top_provinsi,y='total',x='provinsi',height=600)
st.write('Berdasarkan grafik diatas menunjukan jawa barat adalah provinsi yang paling produktif dalam jumlah hasil pertanian,disusul dengan jawa timur dan jawa tengah ')
if st.checkbox('Tabel hasil produksi tani dan pemanasan global Indonesia'):
    top_provinsi

#! line grafik mean temperature vs year
file = open('dataset/mean_temperature.json')
data = json.load(file)
year = []
mean_temperature = []
for key,value in data.items():
    year.append(int(key))
    mean_temperature.append(float(value))

mean_temp = pd.DataFrame({
    'year':year,
    'mean_temp':mean_temperature
})
scaler = preprocessing.MinMaxScaler()
x_scaled = scaler.fit_transform(mean_temp['mean_temp'].values.reshape(-1,1))
x = x_scaled.flatten()
mean_temp = pd.DataFrame({
    'year':year,
    'mean_temp':x
})
st.write('## Grafik tahun dan rata-rata suhu')
st.write('Data berikut ini adalah hasil rata rata suhu tahunan yang telah di normalisasi dengan skala min max yang diambil dari tahun 1900 - 2021 dan dipat dari situs world bank')
st.line_chart(mean_temp,x='year',y='mean_temp')
mean_temp = pd.DataFrame({
    'year':year,
    'mean_temp':mean_temperature
})
st.write('berdasarkan data diatas dapat dilihat bahwa ada kenaikan suhu yang menerus dari 1970 hingga saat ini')
if st.checkbox('Tabel mean year dan mean temperature'):
    mean_temp

#! korelasi mean temperature dengan tahun berjalan
st.write('## Korelasi rata-rata suhu dengan tahun berjalan di indonesia')
st.write('Korelasi dibawah ini didapat dengan menggunakan metode linear regresion')

x = mean_temp['year'].values.reshape(-1,1)

model_2 = LinearRegression()
model_2.fit(x,mean_temp['mean_temp'])

x_vis = np.array([1900,2050]).reshape(-1,1)
y_vis = model_2.predict(x_vis)

fig = plt.figure() 
plt.scatter(x=mean_temp['year'],y=mean_temp['mean_temp'])
plt.plot(x_vis,y_vis,'-r')
plt.xlabel('Tahun Berjalan')
plt.ylabel('mean temperature')
plt.title('korelasi mean temperature dengan tahun berjalan')
st.pyplot(fig)
st.write('Berdasarkan grafik diatas maka dapat diketahui bahwa semakin majunya tahun maka akan dibarengi dengan kenaikan suhu.')

#! hasil tani tahunan
top_anual_value = pd.read_csv('dataset/anual_value.csv')

st.write('## Data produksi hasil pertanian tahunan')
st.write('Berikut ini adalah data produksi hasil 25 jenis hasil pertanian di indonesia dari tahun ke tahun. 25 jenis pertanian diantaranya adalah Bawang Merah, Bawang Putih, Bawang Daun, Kentang, Kubis, Kembang Kol, Petsai/Sawi, Wortel, Lobak, Kacang Merah, Kacang Panjang, Cabai Besar, Cabai Rawit, Tomat, Terung, Buncis, Ketimun, Labu Siam, Kangkung, Bayam, Melinjo, Paprika, Jamur, Petai dan Jengkol.')
st.bar_chart(top_anual_value,y='total',x='date',height=600)
st.write('Berdasarkan grafik diatas total hasil produksi pada tahun 2014 - 2019 mengalami kenaikan cukup tinggi')
if st.checkbox('Tabel produksi hasil pertanian tahunan'):
    top_anual_value

#! korelasi mean temperature dengan kacang merah

mean_temperature = [25.85,25.91,26.04,25.90,25.92,25.93,25.82,25.84,25.71,25.98,26.08,25.88,25.99,26.05,26.04,26.12,26.23,26.03,26.04,26.20,26.18,25.99]

df1 = pd.DataFrame({
    'value': mean_temperature
})
kacang_tanah = pd.read_csv('dataset/kacang_tanah.csv')

df3 = pd.DataFrame({
    'x':df1['value'].values,
    'y':kacang_tanah['total']
})
df3 = df3.head(21)

x = df3['x'].values.reshape(-1,1)


x = df3['x'].values.reshape(-1,1)
y = df3['y']

model = LinearRegression()
model.fit(x,y)

x_vis = np.array([25.65,26.4]).reshape(-1,1)
y_vis = model.predict(x_vis)
st.write('### korelasi mean temperature dengan kacang merah')
st.write('Berikut adalah korelasi hubungan antara suhu rata rata dengan produksi kacang merah di indonesia')
fig = plt.figure() 
plt.scatter(x=df3['x'],y=df3['y'])
plt.plot(x_vis,y_vis,'-r')
plt.xlabel('mean temperature')
plt.ylabel('produksi kacang merah')
plt.title('korelasi mean temperature dengan kacang merah')
st.pyplot(fig)
st.write('berdasarkan grafik diatas terdapat korelasi yang kuat antara suhu rata-rata dengan produksi kacang merah di indonesia.')
if st.checkbox('Tabel suhu rata-rata dengan kacang merah'):
    df3

#! korelasi mean temperature dengan apel malang
df4 = pd.DataFrame({
    'x':df1['value'][3:15],
    'y':[763370,919012,1235569,1255450,1425116,1303299,1291352,842799,777336,748076,838915,708438]
})

x = df4['x'].values.reshape(-1,1)

model_2 = LinearRegression()
model_2.fit(x,df4['y'])

x_vis = np.array([25.65,26.2]).reshape(-1,1)
y_vis = model_2.predict(x_vis)
st.write('### Korelasi mean temperature dengan apel malang')
st.write('Berikut adalah korelasi hubungan antara suhu rata rata dengan produksi apel malang di indonesia')

fig = plt.figure() 
plt.scatter(df4['x'],df4['y'])
plt.plot(x_vis,y_vis,'-r')
plt.xlabel('mean temperature')
plt.ylabel('produksi apel malang')
plt.title('korelasi mean temperature dengan apel malang')
st.pyplot(fig)
st.write('berdasarkan grafik diatas terdapat korelasi yang kuat antara suhu rata-rata dengan produksi apel malang di indonesia.')
if st.checkbox('Tabel suhu rata-rata dan produksi apel malang'):
    df3


#! jenis tani terbanyak sejak tahun 2000 hingga 2022
top_commodity = pd.read_csv('dataset/top_commodity.csv')

st.write('### Jenis hasil tani terbanyak dari tahun 2000 hingga 2021')
st.write('Berikut adalah data jenis hasil 25 produksi pertanian di indonesia')
st.bar_chart(top_commodity,y='total',x='jenis_tani',height=450)
st.write('Berdasarkan grafik diatas tanaman jenis kubis adalah yang tebanyak nilainya')
if st.checkbox('Tabel hasil tani terbanyak dari tahun 2000 hingga 2021'):
    top_commodity

# kata kata diperbaiki, pearson korelasi di cantumkan, dan prediksi berdasarkan suhu