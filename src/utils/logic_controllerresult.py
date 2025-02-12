import model.model_tables as models

def ManipulateData(data_fetch):
    # Inicializar listas vacías correctamente
    name, city, latitude, longitude = [], [], [], []
    price, type_, capacity, rooms_number = [], [], [], []
    bathrooms_number, bedrooms_number, initial_date, end_date = [], [], [], []

    for tuple_result in data_fetch:  # Iterar directamente sobre la lista de tuplas
        name.append(tuple_result[0])
        city.append(tuple_result[1])
        latitude.append(tuple_result[2])
        longitude.append(tuple_result[3])
        price.append(tuple_result[4])
        type_.append(tuple_result[5])  # "type" es una palabra reservada en Python, usamos "type_"
        capacity.append(tuple_result[6])
        rooms_number.append(tuple_result[7])  # Corregido el error de "rooms_numbera"
        bathrooms_number.append(tuple_result[8])
        bedrooms_number.append(tuple_result[9])
        initial_date.append(tuple_result[10])
        end_date.append(tuple_result[11])

    # Crear objeto resultsearch
    data_result = models.resultsearch(
        name=name, city=city, latitude=latitude, longitude=longitude,
        price=price, type=type_, capacity=capacity, rooms_number=rooms_number,
        bathrooms_number=bathrooms_number, bedrooms_number=bedrooms_number,
        initial_date=initial_date, end_date=end_date
    )

    return data_result  # Retornar el objeto resultsearch


