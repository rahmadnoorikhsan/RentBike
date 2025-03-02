# RentBike

## Business Understanding
Pertanyaan bisnis:
1. Pada jam berapa penyewaan sepeda paling banyak dan paling sedikit tersewa?
2. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?
3. Bagaimana pola penyewaan sepeda pada setiap musim?
4. Seberapa besar proporsi customer registered dibandingkan dengan casual?

## Conclusion
1. Penyewaan sepeda paling banyak terjadi pada pukul 17:00, sedangkan paling sedikit pada 04:00 dan rentang 00:00-03:00, menunjukkan pola yang dipengaruhi oleh aktivitas harian.
2. Penyewaan tertinggi terjadi saat cuaca cerah, sementara hujan lebat menyebabkan penurunan signifikan, menunjukkan bahwa cuaca sangat memengaruhi jumlah penyewaan.
3. Musim gugur memiliki penyewaan tertinggi, diikuti oleh musim panas, sedangkan musim semi memiliki penyewaan terendah, menunjukkan preferensi pengguna terhadap cuaca yang lebih nyaman.
4. Proporsi pengguna registered (81.2%) jauh lebih besar dibandingkan casual (18.8%), menunjukkan loyalitas pelanggan tinggi, namun ada peluang meningkatkan pengguna casual dengan promo atau diskon.

## Installation
1. Clone repositori ini ke komputer lokal Anda
```
git clone https://https://github.com/rahmadnoorikhsan/RentBike.git
```
2. Masuk ke direktori proyek
```
cd RentBike
```
3. Instal packages Python yang diperlukan dengan menjalankan perintah berikut:
```
pip install -r requirements.txt
```
## Usage
1. **Data Wrangling**: Gunakan script yang tersedia dalam file `notebook.ipynb` untuk membersihkan dan menyiapkan data sebelum analisis.

2. **Exploratory Data Analysis (EDA)**: Lakukan eksplorasi dan analisis mendalam terhadap data bike-sharing menggunakan script Python yang disediakan. Hasil EDA akan membantu memahami pola penggunaan dan faktor-faktor yang mempengaruhi penyewaan sepeda.

3. **Visualization**: Jalankan dashboard Streamlit untuk menyajikan data secara visual dan interaktif:

```
cd BikeRent/dashboard
streamlit run dashboard.py
```

## Preview
<img src="https://raw.githubusercontent.com/rahmadnoorikhsan/RentBike/refs/heads/main/data/dashboard.png"/>
