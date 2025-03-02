def create_sum_hour_rental(df):
    sum_count_hour_rental = df.groupby("hour").count_rental.sum().sort_values(ascending=False).reset_index()
    return sum_count_hour_rental

def create_rent_by_weather(df):
    rent_by_weather = df.sort_values(by="weather_situation")
    return rent_by_weather

def create_sum_registered_user(df):
    sum_registered_user = df.groupby("date_day").agg({"registered": "sum"}).reset_index()
    return sum_registered_user

def create_sum_casual_user(df):
    sum_casual_user = df.groupby("date_day").agg({"casual": "sum"}).reset_index()
    return sum_casual_user

def create_rent_by_season(df):
    rent_by_season = df.groupby("season").count_rental.sum().reset_index()
    return rent_by_season

def create_calculate_total_customers(df):
    total_casual = df.casual.sum()
    total_registered = df.registered.sum()
    
    return {"casual": total_casual, "registered": total_registered}

def categorize_hour(hour):
    if 6 <= hour < 12:
        return 'Pagi'
    elif 12 <= hour < 18:
        return 'Siang'
    elif 18 <= hour < 24:
        return 'Malam'
    else:
        return 'Dini Hari'


def create_grouped_clustering(df):
    grouped_df = df.groupby(['season', 'holiday', 'weather_situation', 'time_of_day'], observed=False).agg({
        'count_rental': ['mean', 'median', 'std']
    }).reset_index()

    return grouped_df