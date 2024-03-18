vuelo = {
    "Aerolinea": "Avianca",
    "Vuelo": "AV3102",
    "Origen": "Ctg",
    "Destino": "Mde",
    "Tipo_Maleta":['Cabina', 'Mano', 'Bodega']
}

print("valores del diccionario:")
for key, value in vuelo.items():
    print(f"{key}:{value}")
    
    print("\nvalores de tipo de maleta:")
    for maleta in vuelo["Tipo_Maleta"]:
        print(maleta)