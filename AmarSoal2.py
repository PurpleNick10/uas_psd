import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dashboard  # Mengambil DATA_DAY dari dashboard.py

def run():
    st.title("Soal 2")
    st.write("Bagaimana distribusi penggunaan sepeda berdasarkan hari dalam minggu? - 10123179 - Amar Ahmad")

    # Menggunakan dataset dari dashboard
    day = dashboard.DATA_DAY

    st.title("Distribusi Penggunaan Sepeda Berdasarkan Hari dalam Minggu")

    # Membuat plot
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=day, x='weekday', ax=ax)
    ax.set_title('Distribusi Penggunaan Sepeda Berdasarkan Hari dalam Minggu')
    ax.set_xlabel('Hari dalam Minggu')
    ax.set_ylabel('Jumlah')
    ax.set_xticks([0, 1, 2, 3, 4, 5, 6])
    ax.set_xticklabels(['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
