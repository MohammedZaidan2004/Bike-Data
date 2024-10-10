import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Judul Dashboard
st.title("Proyek Analisis Data: Pengaruh Kondisi Cuaca dan Musim Terhadap Jumlah Rental Sepeda")

# Sidebar dengan 3 opsi
option = st.sidebar.selectbox(
    label="Relasi apa yang ingin Anda ketahui terhadap total pengguna rental sepeda?",
    options=['Relasi Total Pengguna Rental Sepeda Berdasarkan Bulan', 
             'Relasi Total Pengguna Rental Sepeda Berdasarkan Kondisi Cuaca', 
             'Relasi Total Pengguna Rental Sepeda Berdasarkan Musim']
)

# Load cleaned dataset
day_df_cleaned = pd.read_csv("C:/Users/masji/OneDrive/Desktop/MLSelfLearn/proyek_analisis_data/day_cleaned.csv", parse_dates=["dteday"])
#day_df_cleaned.info()

# Mengubah dteday ke datetime
day_df_cleaned['dteday'] = pd.to_datetime(day_df_cleaned['dteday'])

# Fungsi untuk menampilkan grafik berdasarkan bulan
def show_month_analysis(df):
    st.header('Relasi Total Pengguna Rental Sepeda Berdasarkan Bulan')
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='mnth', y='cnt', data=df, estimator='mean')
    plt.title('Rata-rata Total Rental Sepeda Berdasarkan Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Rata-rata Total Rental Sepeda')
    st.pyplot(plt.gcf())
    # Insight
    st.subheader('Insight')
    st.write("""
    - Bulan dengan cuaca yang lebih baik, seperti musim panas dan awal musim gugur (Juni hingga September), menunjukkan peningkatan rental sepeda yang signifikan.
    - Aktivitas rental sepeda menurun drastis di musim dingin (Januari), yang bisa dijelaskan oleh kondisi cuaca dingin yang kurang mendukung aktivitas bersepeda.
    """)

# Fungsi untuk menampilkan grafik berdasarkan kondisi cuaca
def show_weather_analysis(df):
    st.header('Relasi Total Pengguna Rental Sepeda Berdasarkan Kondisi Cuaca')
    # Mapping cuaca
    weathersit_labels = {1: 'Clear', 2: 'Mist', 3: 'Light Snow/Light Rain'}
    df['weathersit_label'] = df['weathersit'].map(weathersit_labels)
    weather_group = df.groupby('weathersit_label')['cnt'].sum()

    plt.figure(figsize=(10, 6))
    plt.bar(weather_group.index, weather_group.values, color='lightgreen')
    plt.title('Weather Condition vs Total Rentals')
    plt.xlabel('Weather Condition')
    plt.ylabel('Total Rentals')
    st.pyplot(plt.gcf())
    # Insight
    st.subheader('Insight')
    st.write("""
    - Cuaca yang cerah atau sedikit berawan memiliki pengaruh signifikan terhadap peningkatan jumlah rental sepeda.
    - Aktivitas rental menurun drastis pada kondisi cuaca buruk seperti hujan ringan atau salju, yang menunjukkan bahwa cuaca mempengaruhi kenyamanan dalam bersepeda.
    """)

# Fungsi untuk menampilkan grafik berdasarkan musim
def show_season_analysis(df):
    st.header('Relasi Total Pengguna Rental Sepeda Berdasarkan Musim')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='season', y='cnt', data=df, estimator='mean')
    plt.title('Rata-rata Total Rental Sepeda Berdasarkan Musim')
    plt.xlabel('Musim (1 = Spring, 2 = Summer, 3 = Fall, 4 = Winter)')
    plt.ylabel('Rata-rata Total Rental Sepeda')
    st.pyplot(plt.gcf())
    # Insight
    st.subheader('Insight')
    st.write("""
    - Musim panas (Summer) memiliki jumlah rental sepeda tertinggi, yang menunjukkan kondisi cuaca hangat mendukung aktivitas bersepeda.
    - Musim dingin (Winter) memiliki jumlah rental terendah, menunjukkan bahwa cuaca dingin tidak kondusif untuk bersepeda.
    """)

# Menampilkan analisis sesuai dengan opsi yang dipilih
if option == 'Relasi Total Pengguna Rental Sepeda Berdasarkan Bulan':
    show_month_analysis(day_df_cleaned)
elif option == 'Relasi Total Pengguna Rental Sepeda Berdasarkan Kondisi Cuaca':
    show_weather_analysis(day_df_cleaned)
elif option == 'Relasi Total Pengguna Rental Sepeda Berdasarkan Musim':
    show_season_analysis(day_df_cleaned)
