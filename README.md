# ZINOBE
## Prueba


#### Exercise-Level-2

##### Desarrolle una aplicacion en python que genere la tabla anterior, como se muestra [aquí](https://gitlab.com/eliecer.daza1/zinobe-python-exercises/-/blob/Exercise-Level-2/README.md),  teniendo las siguientes consideraciones:

1. De [https://rapidapi.com/apilayernet/api/rest-countries-v1](https://rapidapi.com/apilayernet/api/rest-countries-v1), obtenga todas las regiones existentes.
2. De [https://restcountries.eu/](https://restcountries.eu/) Obtenga un pais por region apartir de la region optenida del punto 1.
3. De [https://restcountries.eu/](https://restcountries.eu/) obtenga el nombre del idioma que habla el pais y encriptelo con SHA1.
4. En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
5. La tabla debe ser creada en un DataFrame con la libreria PANDAS
6. Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
7. Guarde el resultado en sqlite.
8. Genere un Json de la tabla creada y guardelo como data.json
9. La prueba debe ser entregada en un repositorio git.
10. No usar Framework
11. Usar Test Unitarios
12. Presenta un diseño arquitectonico y de componentes de su solucion.
13. Entregar Dockerfile y docker compose con la solucion, en la que se guarde la data en un docker en mongo.
14. Implemente una autenticacion OAUTH2 para consultar la informacion existente en mongo
15. Documente cómo autenticar y cómo consultar la informacion basado en el punto 14
