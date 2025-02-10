import pandas as pd

# Crear un DataFrame con registros ficticios para la clase Lodging
data = {
    "name": ["Casa Bella", "Sunset Lodge", "Mountain Retreat", "Urban Loft", "Beach House"],
    "city": ["Madrid", "Barcelona", "Zaragoza", "Valencia", "Málaga"],
    "latitude": ["40.4168N", "41.3879N", "41.6488N", "39.4699N", "36.7213N"],
    "longitude": ["3.7038W", "2.1699E", "0.8891W", "0.3763W", "4.4214W"],
    "price": [150, 200, 120, 250, 300],
    "type": ["House", "Lodge", "Cabin", "Apartment", "Villa"],
    "capacity": [4, 6, 5, 3, 8],
    "rooms_number": [3, 4, 3, 2, 5],
    "bathrooms_number": [2, 3, 2, 1, 4],
    "bedrooms_number": [2, 3, 2, 1, 4],
    "id_host": [101, 102, 103, 104, 105]
}

# Convertir a DataFrame
df_lodging = pd.DataFrame(data)
df_lodging.to_csv("df_lodging.csv", index=False)