# Documentación del archivo `agrupados.py`

Este archivo contiene una clase llamada `CrearTabla` que se utiliza para crear una tabla de frecuencias a partir de un conjunto de datos.

## Clase `CrearTabla`

### `__init__(self, datos)`

El constructor de la clase. Toma una lista de datos como entrada.

- `datos`: Una lista de números.

### `calcular_tabla(self, num_clases=None)`

Este método se utiliza para calcular la tabla de frecuencias.

- `num_clases`: El número de clases en las que se dividirán los datos. Si no se proporciona, se calcula utilizando la regla de Scott.

Devuelve un DataFrame de pandas con las siguientes columnas:

- `Clases`: Los límites de cada clase.
- `xi`: El punto medio de cada clase.
- `Frecuencia absoluta`: El número de datos en cada clase.
- `Frecuencia relativa`: La proporción de datos en cada clase.
- `Frecuencia acumulada`: El número acumulado de datos en todas las clases hasta la actual.
- `Frecuencia relativa acumulada`: La proporción acumulada de datos en todas las clases hasta la actual.

### `std(self)`

Este método se utiliza para calcular la desviación estándar de los datos.

### `calcular_límites_clase(self, num_clases)`

Este método se utiliza para calcular los límites de cada clase.

- `num_clases`: El número de clases en las que se dividirán los datos.

### `calcular_puntos_medios(self, límites_clase)`

Este método se utiliza para calcular el punto medio de cada clase.

- `límites_clase`: Una lista con los límites de cada clase.