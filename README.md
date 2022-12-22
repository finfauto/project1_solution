# Proyecto 1

## Parte 1

Disponemos de unos datos de entrada donde se indica en qué posición finalizó un piloto cada Gran Premio de una temporada de la siguiente forma:

```python
driver_season_data = {
        "Bahrain Grand Prix": {
            "position": "1",
            "is_fastestlap": false,
            "bestlap": "00:01:34.015000"
        },
        "Emilia Romagna Grand Prix": {
            "position": "2",
            "is_fastestlap": true,
            "bestlap": "00:01:16.702000"
        },
        "Portuguese Grand Prix": {
            "position": "1",
            "is_fastestlap": false,
            "bestlap": "00:01:20.933000"
        },
        ...
}
```

En dichos datos se echa en falta que se especifique el número de puntos que obtuvo el piloto en cada carrera, por los que nos piden que hagamos un función que complete dicho diccionario añadiendo una clave **points** donde se especifiquen los puntos obtenidos en cada carrera.

Para ello, lo primero que haremos será hacer una función que dada una posición en forma de str y no mediante un tipo int devolverá el número de puntos obtenidos y que tendrá la siguiente forma:

```python
def get_race_points_from_position(position: str) -> float:
    """
    Los puntos a otorgar se reparten según la siguiente tabla:

    | Posición  | Puntos |
    |-----------|--------|
    | "1"       | 25     |
    | "2"       | 18     |
    | "3"       | 15     |
    | "4"       | 12     |
    | "5"       | 10     |
    | "6"       | 8      |
    | "7"       | 6      |
    | "8"       | 4      |
    | "9"       | 2      |
    | "10"      | 1      |
    | otro caso | 0      |
    
    Nota: Aparte de las posición "11", "12" y sucesivas, cuando un piloto se retira su posición será "R"
    """
```

### SOLUCIÓN

Lo primero de todo nos fijamos en el tipo de los parámetros de entrada y reparamos en el primer detalle a tener en cuenta:

**La posición es un string, un caracter, no un número como cabría esperar. Probablemente porque los datos que nos dan también indicarán cuando un piloto no ha acabado la carrera. Si nos vamos a los datos del programa, veremos que efectivamente hay una posición "R" (de retired).**

Otro detalle es que este problema no necesita recorrer ninguna lista ni nigún diccionario. Se nos da una posición y nosotros devolvemos una cantidad de puntos.

Por lo tanto, tenemos que hacer un programa que cuando la entrada sea **"1"** devuelva 25, cuando la entrada sea **"2"** devuelva 18, etc.

**¿Con qué herramienta del lenguaje podemos alcanzar la solución?**

Con un if-else. En este caso, podemos usar la estructura if-elif-else para no generar un código incómodo de leer.

Un detalle de la solución es considerar solamente los puestos del 1 al 10, y agrupar en el else todos los demás puestos, ya que todos esos puestos restantes, sea el que sea, recibirán 0 puntos.


## Parte 2

Los datos nos indican también si el piloto fue el autor de la vuelta rápida. Vamos a hacer una función que nos devuelva los puntos que obtuvo un piloto en la carrera, considerando el punto extra por la vuelta rápido si el piloto quedó entre los 10 primeros.

```python

def get_race_points_from_position_and_fastest_lap(position: int, has_fastest_lap) -> int:
```

### SOLUCIÓN

Esta función es muy similar a la anterior, con el añadido de que por parámetro nos indican si además de la posición del piloto que estamos puntuando, el piloto hizo la vuelta rápida de la carrera, lo que le daría un punto extra.

Podriamos hacer una función desde cero muy similar a la que acabamos de hacer, pero nos va a quedar más elegante si reusamos la que ya hemos hecho.

¿Cuándo hay que dar un punto extra? Cuando has_fastest_lap es True y position <= 10. Pues lo programamos.

```python
    if has_fastest_lap == True and int(position) <= 10:
        return get_race_points_from_position(position) + 1
    return get_race_points_from_position(position)
```

Es decir, en caso de que se cumpla la condición que conocemos para dar el punto de la vuelta rápida, sumamos 1 al resultado que nos da la otra función que hicimos y que nos daba los puntos que obtiene un piloto en una carrera según su posición.

Cuando no se cumple la condición, devolvemos esos puntos directamente.

### OJO

Si ejecutáis esta función tal cual, todavía veréis que hay un test que no pasa (de 42) y que por lo tanto tenéis un error que corregir.

```python
============================= test session starts ==============================
collecting ... collected 42 items

test_world_driver_championship_points.py::test_get_race_points[1-True-26] PASSED [  2%]
test_world_driver_championship_points.py::test_get_race_points[1-False-25] PASSED [  4%]
test_world_driver_championship_points.py::test_get_race_points[2-True-19] PASSED [  7%]
test_world_driver_championship_points.py::test_get_race_points[2-False-18] PASSED [  9%]
test_world_driver_championship_points.py::test_get_race_points[3-True-16] PASSED [ 11%]
test_world_driver_championship_points.py::test_get_race_points[3-False-15] PASSED [ 14%]
test_world_driver_championship_points.py::test_get_race_points[4-True-13] PASSED [ 16%]
test_world_driver_championship_points.py::test_get_race_points[4-False-12] PASSED [ 19%]
test_world_driver_championship_points.py::test_get_race_points[5-True-11] PASSED [ 21%]
test_world_driver_championship_points.py::test_get_race_points[5-False-10] PASSED [ 23%]
test_world_driver_championship_points.py::test_get_race_points[6-True-9] PASSED [ 26%]
test_world_driver_championship_points.py::test_get_race_points[6-False-8] PASSED [ 28%]
test_world_driver_championship_points.py::test_get_race_points[7-True-7] PASSED [ 30%]
test_world_driver_championship_points.py::test_get_race_points[7-False-6] PASSED [ 33%]
test_world_driver_championship_points.py::test_get_race_points[8-True-5] PASSED [ 35%]
test_world_driver_championship_points.py::test_get_race_points[8-False-4] PASSED [ 38%]
test_world_driver_championship_points.py::test_get_race_points[9-True-3] PASSED [ 40%]
test_world_driver_championship_points.py::test_get_race_points[9-False-2] PASSED [ 42%]
test_world_driver_championship_points.py::test_get_race_points[10-True-2] PASSED [ 45%]
test_world_driver_championship_points.py::test_get_race_points[10-False-1] PASSED [ 47%]
test_world_driver_championship_points.py::test_get_race_points[11-True-0] PASSED [ 50%]
test_world_driver_championship_points.py::test_get_race_points[11-False-0] PASSED [ 52%]
test_world_driver_championship_points.py::test_get_race_points[12-True-0] PASSED [ 54%]
test_world_driver_championship_points.py::test_get_race_points[12-False-0] PASSED [ 57%]
test_world_driver_championship_points.py::test_get_race_points[13-True-0] PASSED [ 59%]
test_world_driver_championship_points.py::test_get_race_points[13-False-0] PASSED [ 61%]
test_world_driver_championship_points.py::test_get_race_points[14-True-0] PASSED [ 64%]
test_world_driver_championship_points.py::test_get_race_points[14-False-0] PASSED [ 66%]
test_world_driver_championship_points.py::test_get_race_points[15-True-0] PASSED [ 69%]
test_world_driver_championship_points.py::test_get_race_points[15-False-0] PASSED [ 71%]
test_world_driver_championship_points.py::test_get_race_points[16-True-0] PASSED [ 73%]
test_world_driver_championship_points.py::test_get_race_points[16-False-0] PASSED [ 76%]
test_world_driver_championship_points.py::test_get_race_points[17-True-0] PASSED [ 78%]
test_world_driver_championship_points.py::test_get_race_points[17-False-0] PASSED [ 80%]
test_world_driver_championship_points.py::test_get_race_points[18-True-0] PASSED [ 83%]
test_world_driver_championship_points.py::test_get_race_points[18-False-0] PASSED [ 85%]
test_world_driver_championship_points.py::test_get_race_points[19-True-0] PASSED [ 88%]
test_world_driver_championship_points.py::test_get_race_points[19-False-0] PASSED [ 90%]
test_world_driver_championship_points.py::test_get_race_points[20-True-0] PASSED [ 92%]
test_world_driver_championship_points.py::test_get_race_points[20-False-0] PASSED [ 95%]
test_world_driver_championship_points.py::test_get_race_points[R-True-0] FAILED [ 97%]
test_world_driver_championship_points.py:81 (test_get_race_points[R-True-0])
position = 'R', is_fastest_lap = True, expected_points = 0

    @pytest.mark.parametrize("position, is_fastest_lap, expected_points", testdata_race_points_with_fastest_lap)
    def test_get_race_points(position: str, is_fastest_lap: bool, expected_points: int):
>       assert get_race_points_from_position_and_fastest_lap(position, is_fastest_lap) == expected_points

test_world_driver_championship_points.py:84: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

position = 'R', has_fastest_lap = True

    def get_race_points_from_position_and_fastest_lap(position: str, has_fastest_lap) -> int:
        # PARTE 2
>       if has_fastest_lap == True and int(position) <= 10:
E       ValueError: invalid literal for int() with base 10: 'R'

../world_driver_championship_points.py:49: ValueError
```

Si evaluamos el error da en la línea 49 de nuestro programa, que es esta (como indica el propio error):

```python
if has_fastest_lap == True and int(position) <= 10:
```

También el error dice textualmente:

```bash
E       ValueError: invalid literal for int() with base 10: 'R'
```

Literal inválido para la función **int()**. Vamos, que no es un número y no lo puede transformar como un entero. Así que nos conviene poner un if extra para controlar cuando nos entre una posición "R". Podéis ver cómo lo he controlado en el código de la solución.


## Parte 3

Una vez disponemos de una función que nos indica los puntos que se obtienen según la posición y la vuelta rápida, vamos a hacer una función dadas las carreras realizadas por un piloto en una temporada nos indique el número de puntos que dicho piloto obtuvo esa temporada.

La función tendrá la siguiente interfaz:


```python
def get_driver_season_points(driver_season_data: {}) -> int:
```

El parámetros **season_data** será un diccionario con la siguiente forma:

```python
{
        "Bahrain Grand Prix": {
            "position": 1,
            "is_fastestlap": False,
            "bestlap": "00:01:34.015000"
        },
        "Emilia Romagna Grand Prix": {
            "position": 2,
            "is_fastestlap": True,
            "bestlap": "00:01:16.702000"
        },
        "Portuguese Grand Prix": {
            "position": 1,
            "is_fastestlap": False,
            "bestlap": "00:01:20.933000"
        }
}
```

### SOLUCIÓN

En este caso lo más importante es prestar atención a la entrada de datos. Vemos que es un diccionario en el que vienen una serie de carreras con los resultados de un solo piloto. En la entrada de esta función no nos importa a qué piloto pertenecen estos resultados, simplemente tenemos que recorrer las carreras y calcular los puntos obtenidos en cada una de ellas.

Es un típico problema de acumulador, donde tendremos que ir acumulando los puntos en una variable que devolveremos al final de la función.

Para recorrer un diccionario entero, la forma más común sería:

```python
for race_name, race_data in driver_season_data.items(): 
```

En este caso el nombre de la carrera, que es la clave de cada una de las entradas en el diccionario, no nos importa. Así que sería igual de válido recorrer solamente los valores del diccionario:

```python
for race_data in driver_season_data.values():
```

Y más adelante solamente tendríamos que invocar a la función que ya hicimos y que nos devuelve los puntos de una carrera, pero pasándole los datos de la carrera en la que estamos:

```python
    points_accumulated = 0
    for race_name, race_data in driver_season_data.items():
        points_accumulated = points_accumulated + get_race_points_from_position_and_fastest_lap(race_data["position"], race_data["is_fastestlap"])
    return points_accumulated
```
