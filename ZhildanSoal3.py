import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dashboard  # Mengambil DATA_DAY dari dashboard.py

def run():
    st.title("Soal 3")
    st.write("Apa pengaruh suhu terhadap jumlah sepeda yang digunakan? - 10123188 - Zhildan Saputra")

    # Menggunakan dataset dari dashboard
    day = dashboard.DATA_DAY

    st.title("Pengaruh Suhu Terhadap Jumlah Sepeda yang Digunakan")

    # Membuat scatter plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=day, x='temp', y='cnt', ax=ax)
    ax.set_title('Pengaruh Suhu Terhadap Jumlah Sepeda')
    ax.set_xlabel('Suhu (Celsius)')
    ax.set_ylabel('Jumlah Sepeda')

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
