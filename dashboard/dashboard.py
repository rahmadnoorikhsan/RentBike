import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set_theme(style='dark')
import helper_func

#load data day_clean_df dan hour_clean_df
day_df = pd.read_csv("dashboard/day_clean_df.csv")
hour_df = pd.read_csv("dashboard/hour_clean_df.csv")

# Mengambil min dan max date
min_date = pd.to_datetime(day_df['date_day']).dt.date.min()
max_date = pd.to_datetime(day_df['date_day']).dt.date.max()

# Membuat komponen filter
with st.sidebar:
    # menambahkan logo
    st.image("https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/image1_hH9B4gs.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date])

main_df = day_df[(day_df["date_day"] >= str(start_date)) & 
                (day_df["date_day"] <= str(end_date))]

# Menyiapkan dataframe
sum_count_hour_rental = helper_func.create_sum_hour_rental(hour_df)
rent_by_weather = helper_func.create_rent_by_weather(hour_df)
sum_registered_user = helper_func.create_sum_registered_user(day_df)
sum_casual_user = helper_func.create_sum_casual_user(day_df)
rent_by_season = helper_func.create_rent_by_season(day_df)
calculate_total_customers = helper_func.create_calculate_total_customers(day_df)
grouped_clustering = helper_func.create_grouped_clustering(hour_df)

# Menambahkan judul
st.header('Bike Rent Dashboard')

# Membuat jumlah penyewaan harian
st.subheader('Daily Rent')
col1, col2, col3 = st.columns(3)

with col1:
    total_orders = sum_count_hour_rental.count_rental.sum()
    st.metric("Total Sharing Bike", value=total_orders)

with col2:
    total_sum = sum_registered_user.registered.sum()
    st.metric("Total Registered", value=total_sum)

with col3:
    total_sum = sum_casual_user.casual.sum()
    st.metric("Total Casual", value=total_sum)

# Membuat visualisasi jumlah penyewaan tertinggi dan terendah berdasarkan jam
st.subheader("Best and Worst Hours for Bike Rentals")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(30, 12))

# Warna untuk plot
highlight_color = "#40E0D0"
base_color = "#B0BEC5"
palette_top_hours = [base_color, base_color, highlight_color, base_color, base_color]
palette_bottom_hours = [base_color, base_color, base_color, base_color, highlight_color]

# Plot untuk jam dengan penyewa sepeda tertinggi
sns.barplot(
    x="hour", 
    y="count_rental", 
    data=sum_count_hour_rental.head(5), 
    hue="hour",
    palette=palette_top_hours,
    ax=ax[0]
)
ax[0].set_xlabel("Hours (PM)", fontsize=25, labelpad=15)
ax[0].set_ylabel(None)
ax[0].set_title("Best Hours", fontsize=28)
ax[0].tick_params(axis="x", labelsize=20)
ax[0].tick_params(axis="y", labelsize=20)

# Plot untuk jam dengan penyewa sepeda terendah
sns.barplot(
    x="hour", 
    y="count_rental", 
    data=sum_count_hour_rental.sort_values(by="hour", ascending=True).head(5), 
    hue="hour",
    palette=palette_bottom_hours,
    ax=ax[1]
)
ax[1].set_xlabel("Hours (AM)", fontsize=25, labelpad=15)
ax[1].set_ylabel(None)
ax[1].set_title("Worst Hours", fontsize=28)
ax[1].tick_params(axis="x", labelsize=20)
ax[1].tick_params(axis="y", labelsize=20)
ax[1].invert_xaxis()

st.pyplot(fig)

# Membuat visualisasi penjualan berdasarkan cuaca
st.subheader("Weather Impact on Bike Rentals")
fig, ax = plt.subplots(figsize=(20, 10))

# Warna untuk plot
palette_weather = [highlight_color, base_color, base_color, base_color]

# Membuat barplot
sns.barplot(
    y="count_rental", 
    x="weather_situation",
    data=rent_by_weather,
    hue="weather_situation",
    palette=palette_weather,
    ax=ax,
    errorbar=None
)
ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)

st.pyplot(fig)

# Membuat visualisasi pola penyewaan berdasarkan musim
st.subheader("Seasonal Trends in Bike Rentals")

fig, ax = plt.subplots(figsize=(20, 10))

# Warna untuk plot
palette_season = [base_color, base_color, highlight_color, base_color]

# Membuat barplot
sns.barplot(
    y="count_rental", 
    x="season",
    data=day_df,
    palette=palette_season,
    hue="season",
    ax=ax,
    errorbar=None
)

# Mengatur judul, label, dan tampilan grafik
ax.set_title("Bike Rentals by Season", fontsize=25, loc="center")
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)

st.pyplot(fig)

# Membuat visualisasi Proporsi customer registered dan casual
st.subheader("Comparison of Registered vs Casual Customers")

labels = 'casual', 'registered'
colors = ["#D3D3D3", "#40E0D0"]
data = [calculate_total_customers["casual"], calculate_total_customers["registered"]]

fig, ax = plt.subplots()

ax.pie(
    data,
    labels=labels, 
    autopct='%1.1f%%', 
    colors=colors, 
    startangle=140, 
    explode=(0.05, 0)
)

st.pyplot(fig)

# Membuat visualisasi clustering
st.subheader("Rental Demographics")
 
col1, col2 = st.columns(2)
 
# Visualisasi jumlah peminjaman rata-rata berdasarkan musim
with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
    
    sns.barplot(data=grouped_clustering, x='season', y=('count_rental', 'mean'), hue='time_of_day', errorbar=None)
    ax.set_title("Average Bike Rentals per Season", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.legend(title='Time of Day')
    ax.tick_params(axis='y', labelsize=30)
    ax.tick_params(axis='x', labelsize=35)
    st.pyplot(fig)
 
# Visualisasi jumlah peminjaman rata-rata berdasarkan cuaca
with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    
    sns.barplot(data=grouped_clustering, x='weather_situation', y=('count_rental', 'mean'), hue='time_of_day', errorbar=None)
    ax.set_title("Average Bike Rentals by Weather", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.legend(title='Time of Day')
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

# Visualisasi jumlah peminjaman rata-rata pada hari libur dan non-libu
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(data=grouped_clustering, x='holiday', y=('count_rental', 'mean'), hue='time_of_day', errorbar=None)
ax.set_title("Average Bike Rentals on Holidays vs Workdays", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.legend(title='Time of Day')
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=25)
st.pyplot(fig)
