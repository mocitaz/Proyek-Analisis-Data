import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("main_data.csv")

# Judul
st.title("Dashboard Penyewaan Sepeda")

# Visualisasi 1: Hari Kerja vs Libur
st.subheader("Penyewaan Berdasarkan Hari Kerja vs Libur")
workingday_group = data.groupby('workingday')['cnt'].mean()
fig, ax = plt.subplots()
workingday_group.plot(kind='bar', ax=ax, color=['blue', 'orange'])
ax.set_title('Rata-rata Penyewaan')
ax.set_xlabel('Hari Kerja (0 = Libur, 1 = Kerja)')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Visualisasi 2: Cuaca
st.subheader("Penyewaan Berdasarkan Cuaca")
fig, ax = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=data, ax=ax)
ax.set_title('Rata-rata Penyewaan Berdasarkan Cuaca')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)