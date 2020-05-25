from hashlib import sha1

import json
import pandas as pd 
import requests
import timeit


def obtener_regiones():

    regiones = []
    headers = {"x-rapidapi-host": "restcountries-v1.p.rapidapi.com","x-rapidapi-key": "138bf105acmsh9559d0aa02b5a31p15c933jsn73b13c1900e8"}
    res = requests.get('https://restcountries-v1.p.rapidapi.com/all', headers=headers)
    res = res.json()
    for i in res:
        if i['region'] not in regiones and i['region'] is not '':
            regiones.append(i['region'])
        return regiones

#=============================InicioTest
#PROBANDO LA FUNCIÓN obtener_regiones
regions = []
headers = {"x-rapidapi-host": "restcountries-v1.p.rapidapi.com","x-rapidapi-key": "138bf105acmsh9559d0aa02b5a31p15c933jsn73b13c1900e8"}
res = requests.get('https://restcountries-v1.p.rapidapi.com/all', headers=headers)
res = res.json()
for i in res:
    if i['region'] not in regions and i['region'] is not '':
        regions.append(i['region'])
print(regions)
print(headers)
print(res)
print(res[1])
print(res[10]['region'])
print(regions)
#=============================FinTest


def obtener_pais_por_region(region):

    tiempo_inicial = timeit.timeit()
    region = region
    res = requests.get(f'https://restcountries.eu/rest/v2/region')
    res = res.json()
    tiempo_final = timeit.timeit()
    tiempo_total = (tiempo_final - tiempo_inicial)*1000
    pais = {'region': region, 'name': res[0]['name'], 'language': encode_sha1(res[0]['languages'][0]['name']), 'time': tiempo_total}
    return pais

#=============================InicioTest
#PROBANDO LA FUNCIÓN obtener_pais_por_region

t_i = timeit.timeit()
print(t_i)
headers = {"x-rapidapi-host": "restcountries-v1.p.rapidapi.com","x-rapidapi-key": "138bf105acmsh9559d0aa02b5a31p15c933jsn73b13c1900e8"}
res = requests.get('https://restcountries-v1.p.rapidapi.com/all', headers=headers)
res = res.json()
pais = {'region': region, 'name': res[0]['name'], 'language': encode_sha1(res[0]['languages'][0]['name']), 'time': tiempo_total}


#una solución es cambiar el json en un dictionario, eliminar los elemenos que no me sirven, cambiar el lenguaje, y luego filtrarlo. 

#a = {1:1, 2:2, 3:3}
#>>> dict((key,value) for key, value in a.iteritems() if key == 1)
#{1: 1}


tiempo_final = timeit.timeit()
tiempo_total = (tiempo_final - tiempo_inicial)*1000
pais = {'region': region, 'name': res[0]['name'], 'language': encode_sha1(res[0]['languages'][0]['name']), 'time': tiempo_total}
print(pais)
#=============================FinTest


def calculo_tiempo_ejecucion(lst):
    """
    Cálculo del tiempo de ejecución de acuerdo al punto 4 de la prueba, 
    creando la tabla en un dataframe de pandas de acuerdo al punto 5, 
    y mostrando los tiempos (máximo, mínimo, promedio y total) de acuerdo al punto 6.
    Punto 4:
    En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico).
    Punto 5:
    La tabla debe ser creada en un DataFrame con la libreria PANDAS.
    Punto 6:
    Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
    """
    df = pd.DataFrame(lst)
    try:
        tiempo_total, tiempo_promedio =  df["time"].sum(), df["time"].mean()
        tiempo_min, tiempo_max = df["time"].min(), df["time"].max()
    except KeyError:
        return "error: Dataframe doesn't have the column required"
    return tiempo_total, tiempo_promedio, tiempo_min, tiempo_max

def paises_json(lst):
    with open('data.json', 'w') as json_file:
        json.dump(lst, json_file)


