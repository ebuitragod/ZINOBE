from paises import obtener_regiones, obtener_pais_por_region, calculo_tiempo_ejecucion, paises_json, encode_sha1
import pytest


def test_obtener_regiones():
    res = obtener_regiones()
    assert res == ['Asia', 'Europe', 'Africa', 'Oceania', 'Americas', 'Polar']

def test_obtener_pais_por_region():
    region = 'asia'
    res = obtener_pais_por_region('asia')
    assert res['name'] == 'Afghanistan'
    assert res['region'] == 'asia'

def test_encode_sha1_integer():
    res = encode_sha1(1)
    assert 'error' in res.keys() 
    assert res['error'] == 'parameter provided is not a string'

def test_encode_sha1_string():
    res = encode_sha1("test")
    assert type(res) == str
    assert 'keys' not in dir(res)

def test_paises_json():
    lst = [1,2,3,4]
    res = paises_json(lst)
    import os.path
    assert os.path.exists('data.json') == True

def test_calculo_tiempo_ejecucion_wrong_list():
    lst = ['1', 2, 3, 4 ]
    res = calculo_tiempo_ejecucion(lst)
    assert res == "error: Dataframe doesn't have the column required"








