# Bike Sharing Data Analysis Dashboard 🚴‍♂️

## Deskripsi

Dashboard ini dibuat untuk melakukan analisis data terkait sharing sepeda. Dashboard ini memungkinkan Anda untuk menjawab dua pertanyaan bisnis utama:

1. Bagaimana pola sewa sepeda berubah berdasarkan musim?
2. Bagaimana pengaruh suhu (temperature) terhadap jumlah sewa sepeda?

Dashboard ini menggunakan data dari file "main_data.csv" yang telah disiapkan. Anda dapat menjalankan dashboard ini secara lokal dengan mengikuti langkah-langkah di bawah ini.

## Setup Lingkungan

Sebelum Anda menjalankan dashboard, pastikan Anda memiliki lingkungan yang sesuai dengan paket-paket yang diperlukan. Anda dapat membuat lingkungan virtual dengan Python 3.9 dan menginstal paket-paket yang diperlukan menggunakan `pip` sebagai berikut:

```bash
conda create --name bike-sharing python=3.9
conda activate bike-sharing
pip install pandas matplotlib seaborn streamlit
```

## Menjalankan Dashboard

Setelah Anda memiliki lingkungan yang sesuai, Anda dapat menjalankan dashboard dengan perintah berikut:

```bash
streamlit run dashboard.py
```