import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dashboard  # Mengambil DATA_DAY dari dashboard.py

def run():
    st.title("Soal 5")
    st.write("Apakah terdapat perbedaan penggunaan sepeda antara hari kerja dan akhir pekan? - 10123198 - Arswandi Raditya R. Sunusi")

    # Menggunakan dataset dari dashboard
    day = dashboard.DATA_DAY.copy()  # Gunakan salinan agar tidak mengubah data asli

    st.title("Perbandingan Penggunaan Sepeda pada Hari Kerja dan Akhir Pekan")

    # Menambahkan kolom is_weekend (True jika Sabtu/Minggu, False jika hari kerja)
    day['is_weekend'] = day['weekday'].isin([5, 6])  

    # Membuat boxplot
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=day, x='is_weekend', y='cnt', ax=ax)
    ax.set_title('Perbandingan Penggunaan Sepeda Antara Hari Kerja dan Akhir Pekan')
    ax.set_xlabel('Akhir Pekan (True/False)')
    ax.set_ylabel('Jumlah Sepeda')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Hari Kerja', 'Akhir Pekan'])

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
