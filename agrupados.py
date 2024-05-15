import pandas as pd

class CrearTabla:
    def __init__(self, datos):
        self.datos = datos
        self.num_datos = len(datos)
        
    def calcular_tabla(self, num_clases=None):
        if num_clases is None:
            # Calcular el número de clases utilizando la regla de Scott
            ancho_banda = 3.5 * self.datos['xi'].std() / (self.num_datos ** (1/2))
            num_clases = int((max(self.datos['xi']) - min(self.datos['xi'])) / ancho_banda)
        
        # Calcular los límites de clase
        límites_clase = self.calcular_límites_clase(num_clases)
        
        # Calcular las frecuencias absolutas
        frecuencias_absolutas = pd.cut(self.datos['xi'], límites_clase, include_lowest=True, right=False).value_counts().sort_index().tolist()
        
        # Calcular frecuencia relativa
        frecuencia_relativa = [round(f / self.num_datos, 1) for f in frecuencias_absolutas]
        
        # Calcular frecuencia acumulada
        frecuencia_acumulada = pd.Series(frecuencias_absolutas).cumsum().tolist()
        
        # Calcular frecuencia relativa acumulada
        frecuencia_relativa_acumulada = pd.Series(frecuencia_relativa).cumsum().tolist()
        
        # Calcular el punto medio de cada clase
        puntos_medios = self.calcular_puntos_medios(límites_clase)
        
        # Crear DataFrame para la tabla de frecuencia
        tabla = pd.DataFrame({
            'Clases': [f"{round(límites_clase[i], 1)} - {round(límites_clase[i+1], 1)}" for i in range(len(límites_clase) - 1)],
            'xi': [round(x, 1) for x in puntos_medios],
            'Frecuencia absoluta': frecuencias_absolutas,
            'Frecuencia relativa': frecuencia_relativa,
            'Frecuencia acumulada': frecuencia_acumulada,
            'Frecuencia relativa acumulada': frecuencia_relativa_acumulada
        })
        
        return tabla

    def calcular_media(self):
        media = round(sum(self.datos['xi']) / self.num_datos, 1)
        return media

    def calcular_varianza(self):
        media = self.calcular_media()
        suma = sum((xi - media) ** 2 for xi in self.datos['xi'])
        varianza = round(suma / self.num_datos, 1)
        return varianza

    def calcular_límites_clase(self, num_clases):
        epsilon = 1e-10  # Un pequeño valor para ajustar los límites de las clases
        min_dato = min(self.datos['xi']) - epsilon
        max_dato = max(self.datos['xi']) + epsilon
        ancho_clase = (max_dato - min_dato) / num_clases
        límites_clase = [min_dato + i * ancho_clase for i in range(num_clases + 1)]
        return límites_clase

    def calcular_puntos_medios(self, límites_clase):
        return [(límites_clase[i] + límites_clase[i+1]) / 2 for i in range(len(límites_clase) - 1)]