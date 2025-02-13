import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dashboard  # Mengimpor modul dashboard untuk mengambil DATA_DAY

def run():
    st.title("Soal 1")
    st.write("Berdasarkan data, musim apa yang paling sering dipilih orang untuk bersepeda? - 10123175 - Riansyah Fahrial Azwani")

    # Menggunakan dataset dari dashboard
    day = dashboard.DATA_DAY

    st.title("Distribusi Jumlah Sepeda Berdasarkan Musim")

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=day, x='season', ax=ax)
    ax.set_title('Distribusi Jumlah Sepeda Berdasarkan Musim')
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah')
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(['Musim Dingin', 'Musim Semi', 'Musim Panas', 'Musim Gugur'])

    # Tampilkan plot di Streamlit
    st.pyplot(fig)
