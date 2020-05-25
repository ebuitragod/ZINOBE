import requests_cache
from country import calc_exec_times, countries_to_json, get_first_country_by_region, get_regions
from database import insert_countries

# Initialize cache
requests_cache.install_cache('country_cache', backend='sqlite', expire_after=600) 

if __name__ == "__main__":
    """
    1. Obtener las regiones del servicio API.
    2. Empezamos construyendo la información para cada país
    3. Mostrando los tiempos de ejecución AL usuario.
    4. Inserción de la información del país.
    5. Exportación de la información en un json
    """
    countries = []
    regions = get_regions()
    for i in regions:
        country = get_first_country_by_region(i)
        countries.append(country)
    total_tm, avrg_tm, min_tm, max_tm = calc_exec_times(countries)
    print(f'Total time: {total_tm} ms\nMean time: {avrg_tm} ms\n')
    print(f'Minimum time: {min_tm} ms\nMaximum time: {max_tm} ms\n')
    insert_countries(countries)
    countries_to_json(countries)