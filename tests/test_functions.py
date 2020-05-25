from functions_countries import get_regions, get_country_by_region, encode_sha1, execution_time, countries_json
import pytest


def test_get_regions():
    obj = get_regions()
    assert obj == ['Asia', 'Europe', 'Africa', 'Oceania', 'Americas', 'Polar']

obj_region = get_regions()
obj_country_by_region = get_country_by_region(obj_region)
print(obj_country_by_region)

def test_get_country_by_region():
    region = 'Asia'
    res = get_country_by_region('asia')
    assert res['name'] == 'Yemen'
    assert res['region'] == 'Asia'

# def test_get_country_by_region():
#     region = 'Asia'
#     res = get_country_by_region('asia')
#     assert res['name'] == 'Afghanistan'
#     assert res['region'] == 'Asia'

# def test_encode_sha1_integer():
#     res = encode_sha1(1)
#     assert 'error' in res.keys() 
#     assert res['error'] == 'parameter provided is not a string'

# def test_encode_sha1_string():
#     res = encode_sha1("test")
#     assert type(res) == str
#     assert 'keys' not in dir(res)

# def test_countries_json():
#     lst = [1,2,3,4]
#     res = countries_json(lst)
#     import os.path
#     assert os.path.exists('data.json') == True

# def test_execution_time_wrong_list():
#     lst = ['1', 2, 3, 4 ]
#     res = execution_time(lst)
#     assert res == "error: Dataframe doesn't have the column required"








