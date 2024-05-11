import pandas as pd
from tabulate import tabulate

class CrearTabla:
    def __init__(self, datos):
        self.datos = datos
        self.num_datos = len(datos)
        
    def calcular_tabla(self, num_clases=None):
        if num_clases is None:
            # Calcular el número de clases utilizando la regla de Scott
            ancho_banda = 3.5 * self.std() / (self.num_datos ** (1/3))
            num_clases = int((max(self.datos) - min(self.datos)) / ancho_banda)
        
        # Calcular los límites de clase
        límites_clase = self.calcular_límites_clase(num_clases)
        
        # Calcular las frecuencias
        frecuencias = self.calcular_frecuencias(límites_clase)
        
        # Calcular frecuencia relativa
        frecuencia_relativa = frecuencias / self.num_datos
        
        # Calcular frecuencia acumulada
        frecuencia_acumulada = frecuencias.cumsum()
        
        # Calcular frecuencia relativa acumulada
        frecuencia_relativa_acumulada = frecuencia_relativa.cumsum()
        
        # Calcular el punto medio de cada clase
        puntos_medios = self.calcular_puntos_medios(límites_clase)
        
        # Crear DataFrame para la tabla de frecuencia
        tabla = pd.DataFrame({
            'Límite inferior': límites_clase[:-1],
            'Límite superior': límites_clase[1:],
            'Punto medio': puntos_medios,
            'Frecuencia absoluta': frecuencias,
            'Frecuencia relativa': frecuencia_relativa,
            'Frecuencia acumulada': frecuencia_acumulada,
            'Frecuencia relativa acumulada': frecuencia_relativa_acumulada
        })
        
        return tabla
    
    def std(self):
        mean = sum(self.datos) / self.num_datos
        variance = sum((x - mean) ** 2 for x in self.datos) / self.num_datos
        return variance ** 0.5
    
    def calcular_límites_clase(self, num_clases):
        min_dato = min(self.datos)
        max_dato = max(self.datos)
        ancho_clase = (max_dato - min_dato) / num_clases
        return [min_dato + i * ancho_clase for i in range(num_clases + 1)]

    def calcular_frecuencias(self, límites_clase):
        frecuencias = [0] * (len(límites_clase) - 1)
        for dato in self.datos:
            for i, límite in enumerate(límites_clase[:-1]):
                if dato >= límite and dato < límites_clase[i+1]:
                    frecuencias[i] += 1
                    break
        return frecuencias

    def calcular_puntos_medios(self, límites_clase):
        return [(límites_clase[i] + límites_clase[i+1]) / 2 for i in range(len(límites_clase) - 1)]
