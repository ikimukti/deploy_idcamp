import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the merged data from 'main_data.csv'
main_data = pd.read_csv("dashboard/main_data.csv")

# Set the page title and description
st.set_page_config(page_title="Bike Sharing Dashboard", page_icon="🚴‍♂️")
st.title("Bike Sharing Data Analysis")

# Sidebar for user inputs
st.sidebar.header("User Inputs")
selected_question = st.sidebar.selectbox("Pilih Pertanyaan Bisnis:", ["Pertanyaan 1", "Pertanyaan 2"])

# Define functions for data visualization based on user selection
def plot_seasonal_pattern():
    st.subheader("Pertanyaan 1: Bagaimana pola sewa sepeda berubah berdasarkan musim?")
    
    # Visualisasi jumlah sewa sepeda per musim
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='season_hourly', y='cnt_hourly', data=main_data, ax=ax)  # Mengganti 'season' dengan 'season_hourly'
    ax.set_title('Distribusi Jumlah Sewa Sepeda per Musim')
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Sewa Sepeda')
    ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
    st.pyplot(fig)

def plot_temperature_effect():
    st.subheader("Pertanyaan 2: Bagaimana pengaruh suhu (temperature) terhadap jumlah sewa sepeda?")
    
    # Visualisasi pengaruh suhu terhadap jumlah sewa sepeda
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(main_data['temp_hourly'], main_data['cnt_hourly'], alpha=0.5)
    ax.set_title('Pengaruh Suhu terhadap Jumlah Sewa Sepeda')
    ax.set_xlabel('Suhu (Normalized)')
    ax.set_ylabel('Jumlah Sewa Sepeda')
    st.pyplot(fig)

# Based on user selection, call the appropriate function
if selected_question == "Pertanyaan 1":
    plot_seasonal_pattern()
elif selected_question == "Pertanyaan 2":
    plot_temperature_effect()
