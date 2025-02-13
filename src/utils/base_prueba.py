import pandas as pd

# Crear un DataFrame con registros ficticios para la clase Lodging
data = {
    "name": [
        "Apartamento Moderno", "Casa Colonial", "Cabaña Rústica", "Loft Lujoso", "Villa Marítima",
        "Casa Campestre", "Penthouse Exclusivo", "Refugio en la Montaña", "EcoLodge Selva", "Hacienda Tradicional",
        "Bungalow Azul", "Casa del Lago", "Estudio Urbano", "Cabaña del Bosque", "Hotel Boutique",
        "Hostal Bohemio", "Chalet Alpino", "Casa del Sol", "Apartamento Ejecutivo", "Finca Cafetera",
        "Villa Romántica", "Cabaña del Río", "Resort de Lujo", "Casa Mirador", "Glamping Estelar"
    ],
    "city": [
        "Bogotá", "Cartagena", "Armenia", "Medellín", "Santa Marta",
        "Villavicencio", "Cali", "Manizales", "Leticia", "Pereira",
        "San Andrés", "Guatapé", "Bucaramanga", "Popayán", "Barranquilla",
        "Santa Marta", "Tunja", "Neiva", "Pasto", "Armenia",
        "Cúcuta", "Ibagué", "Montería", "Manizales", "Boyacá"
    ],
    "price": [
        120, 250, 90, 180, 300,
        140, 275, 100, 85, 230,
        320, 210, 150, 110, 400,
        95, 170, 160, 200, 220,
        130, 190, 350, 280, 140
    ],
    "type": [
    "Apartamento", "Casa", "Casa", "Casa", "Apartamento",
    "Casa de huéspedes", "Apartamento", "Casa", "Casa", "Casa",
    "Casa de huéspedes", "Casa de huéspedes", "Casa", "Casa de huéspedes", "Casa de huéspedes",
    "Apartamento", "Apartamento", "Casa", "Apartamento", "Casa de huéspedes",
    "Casa de huéspedes", "Casa", "Apartamento", "Casa", "Apartamento"
    ],
    "capacity": [
        4, 8, 6, 2, 10,
        6, 5, 4, 3, 12,
        7, 9, 2, 5, 15,
        10, 6, 5, 3, 12,
        8, 7, 20, 6, 4
    ],
    "rooms_number": [
        2, 4, 3, 1, 5,
        3, 4, 2, 2, 6,
        3, 5, 1, 2, 8,
        5, 3, 3, 2, 5,
        4, 3, 10, 3, 2
    ],
    "bathrooms_number": [
        2, 3, 2, 1, 4,
        2, 3, 1, 1, 4,
        2, 3, 1, 1, 5,
        3, 2, 2, 1, 3,
        2, 2, 8, 2, 1
    ],
    "bedrooms_number": [
        2, 4, 3, 1, 5,
        3, 4, 2, 2, 6,
        3, 5, 1, 2, 8,
        4, 3, 3, 2, 5,
        4, 3, 9, 3, 2
    ]
}

# Convertir a DataFrame
df_lodging = pd.DataFrame(data)
df_lodging.to_csv("df_lodging.csv", index=False)