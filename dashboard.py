import streamlit as st
import pandas as pd
import RianSoal1
import AmarSoal2
import ZhildanSoal3
import RazanSoal4
import WandiSoal5
import BramSoal6

# Navbar
st.sidebar.title("BAR NAVIGASI")
option = st.sidebar.radio(
    "Pemilihan Halaman:", 
    ("Home", "Soal 1", "Soal 2", "Soal 3", "Soal 4", "Soal 5", "Soal 6"), 
    key="sidebar_menu"
)

# Load dataset
day = pd.read_csv('day.csv')
hour = pd.read_csv('hour.csv')

# Data Cleaning
day = day.dropna().dropna(axis=1).drop_duplicates()
hour = hour.dropna().dropna(axis=1).drop_duplicates()

# Konversi kolom tanggal
day['dteday'] = pd.to_datetime(day['dteday'])
day['month'] = day['dteday'].dt.month

# Simpan hasil cleaning agar bisa digunakan di Soal 1
day.to_csv('day_cleaned.csv', index=False)
hour.to_csv('hour_cleaned.csv', index=False)

# Menyediakan dataset agar bisa diimpor ke soal lain
DATA_DAY = day
DATA_HOUR = hour

# Tampilkan halaman sesuai pilihan
if option == "Home":
    st.title("KELOMPOK 4")
    st.title("Analisis day.csv dan hour.csv untuk tugas UAS")
    st.write("Nama Anggota:")
    st.write("[Riansyah Fahrial Azwani    - 10123175]")
    st.write("[Amar Ahmad                 - 10123179]")
    st.write("[Zhildan Saputra            - 10123188]")
    st.write("[Razan Rijalul Fiqri        - 10123189]")
    st.write("[Arswandi Raditya R. Sunusi - 10123198]")
    st.write("[Bramantio Dewangga         - 10123210]")

elif option == "Soal 1":
    RianSoal1.run()

elif option == "Soal 2":
    AmarSoal2.run()
    
elif option == "Soal 3":
    ZhildanSoal3.run()

elif option == "Soal 4":
    RazanSoal4.run()

elif option == "Soal 5":
    WandiSoal5.run()

elif option == "Soal 6":
    BramSoal6.run()
