import requests
import json
import pandas as pd
import numpy as np
from funciones import normalizar_nombre

url = 'https://servicios.ine.es/wstempus/jsCache/ES/DATOS_TABLA/'
Ipc_code = '50913'
response = requests.get(url+Ipc_code).json()

ids_names = {
    0 : 'España',
    1 : 'Andalucía',
    2 : 'Aragón',
    3 : 'Principado de Asturias',
    4 : 'Islas Baleares',
    5 : 'Islas Canarias',
    6 : 'Cantabria',
    7 : 'Castilla y León',
    8 : 'Castilla La Mancha',
    9 : 'Cataluña',
    10 : 'Comunidad Valenciana',
    11 : 'Extremadura',
    12 : 'Galicia',
    13 : 'Comunidad de Madrid',
    14 : 'Región de Murcia',
    15 : 'Comunidad Foral de Navarra',
    16 : 'País Vasco',
    17 :'La Rioja',
    18 :'Ceuta',
    19 :'Melilla',
}

df = pd.DataFrame(columns=['city','Agno','Mes','Value'])

# En el dataset hay muchos datos, nos centramos en el IPC total de cada Comunidad autónoma
# IPC Total = en el nombre --> [' Índice general', ' Índice']
counter = 0
for x,i in enumerate(response.json()):
    if i['Nombre'].split('.')[1:3] == [' Índice general', ' Índice']:
        nombre = i['Nombre'].split('.')[0]
        id = normalizar_nombre(nombre)
        city_data = response.json()[x]['Data']
        for row in city_data:
            df.loc[counter] = [int(id), row['Anyo'], row['FK_Periodo'], row['Valor']]
            counter += 1

df['city'] = df['city'].astype(np.int64)
df['Mes'] = df['Mes'].astype(np.int64)
df['Agno'] = df['Agno'].astype(np.int64)
df.to_csv('IPC.csv', index=False)

df_index = pd.DataFrame(list(ids_names.items()), columns=['ID', 'Nombre'])
df_index.to_csv('indices.csv', index=False)

"""
Si queremos en vez del IPC en general, algo como los alimentos y las bebidas no alcoholicas
solo hay que cambiar la label:

sample:
if i['Nombre'].split('.')[1:3] == [' Alimentos y bebidas no alcohólicas', ' Índice']:


LABELS:
- Índice general
- Alimentos y bebidas no alcohólicas
- Bebidas alcohólicas y tabaco
- Vestido y calzado
- Vivienda, agua, electricidad, gas y otros combustibles
- Muebles, artículos del hogar y artículos para el mantenimiento corriente del hogar
- Sanidad
- Transporte
- Comunicaciones
- Ocio y cultura
- Enseñanza
- Restaurantes y hoteles
- Otros bienes y servicios


"""