import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dashboard  # Mengambil DATA_DAY dari dashboard.py

def run():
    st.title("Soal 6")
    st.write("Bagaimana pengaruh hari dalam seminggu terhadap suhu yang tercatat? - 10123210 - Bramantio Dewangga")

    # Menggunakan dataset dari dashboard
    day = dashboard.DATA_DAY.copy()  # Gunakan salinan agar tidak mengubah data asli

    st.title("Pengaruh Hari dalam Minggu Terhadap Suhu")

    # Membuat boxplot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=day, x='weekday', y='temp', ax=ax)
    ax.set_title('Pengaruh Hari dalam Minggu Terhadap Suhu')
    ax.set_xlabel('Hari dalam Minggu')
    ax.set_ylabel('Suhu (Celsius)')
    ax.set_xticks([0, 1, 2, 3, 4, 5, 6])
    ax.set_xticklabels(['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
