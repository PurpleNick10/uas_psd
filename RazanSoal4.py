import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dashboard  # Mengambil DATA_DAY dari dashboard.py

def run():
    st.title("Soal 4")
    st.write("Bagaimana distribusi jumlah sepeda berdasarkan situasi cuaca? - 10123189 - Razan Rijalul Fiqri")

    # Menggunakan dataset dari dashboard
    day = dashboard.DATA_DAY

    st.title("Distribusi Jumlah Sepeda Berdasarkan Situasi Cuaca")

    # Membuat count plot
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=day, x='weathersit', ax=ax)
    ax.set_title('Distribusi Jumlah Sepeda Berdasarkan Situasi Cuaca')
    ax.set_xlabel('Situasi Cuaca')
    ax.set_ylabel('Jumlah')
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(['Cerah', 'Berawan', 'Hujan'])

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
