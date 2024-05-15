import pandas as pd
import numpy as np

class CrearTabla:
    def __init__(self, datos):
        self.datos = pd.DataFrame({'xi': datos})
        self.num_datos = len(datos)

    def calcular_tabla(self, num_clases=None):
        if num_clases is None:
            ancho_banda = 3.5 * self.datos['xi'].std() / (self.num_datos ** (-1/3))
            num_clases = int(np.ceil((max(self.datos['xi']) - min(self.datos['xi'])) / ancho_banda))
        
        límites_clase = self.calcular_límites_clase(num_clases)
        frecuencias_absolutas = pd.cut(self.datos['xi'], límites_clase, include_lowest=True, right=False).value_counts().sort_index().tolist()
        frecuencia_relativa = [round(f / self.num_datos, 4) for f in frecuencias_absolutas]
        frecuencia_acumulada = pd.Series(frecuencias_absolutas).cumsum().tolist()
        frecuencia_relativa_acumulada = pd.Series(frecuencia_relativa).cumsum().tolist()
        puntos_medios = self.calcular_puntos_medios(límites_clase)
        
        tabla = pd.DataFrame({
            'Clases': [f"{round(límites_clase[i], 1)} - {round(límites_clase[i+1], 1)}" for i in range(len(límites_clase) - 1)],
            'xi': [round(x, 1) for x in puntos_medios],
            'Frecuencia absoluta': frecuencias_absolutas,
            'Frecuencia relativa': frecuencia_relativa,
            'Frecuencia acumulada': frecuencia_acumulada,
            'Frecuencia relativa acumulada': [round(x, 4) for x in frecuencia_relativa_acumulada]
        })
        
        return tabla

    def calcular_media(self):
        media = round(self.datos['xi'].mean(), 1)
        return media

    def calcular_mediana(self):
        mediana = round(self.datos['xi'].median(), 1)
        return mediana

    def calcular_moda(self):
        moda = self.datos['xi'].mode()
        if len(moda) > 1:
            return [round(m, 1) for m in moda]
        else:
            return round(moda.iloc[0], 1)

    def calcular_varianza(self):
        varianza = round(self.datos['xi'].var(ddof=0), 1)
        return varianza

    def calcular_desviacion_estandar(self):
        desviacion_estandar = round(self.datos['xi'].std(ddof=0), 1)
        return desviacion_estandar

    def calcular_límites_clase(self, num_clases):
        min_dato = self.datos['xi'].min()
        max_dato = self.datos['xi'].max()
        ancho_clase = (max_dato - min_dato) / num_clases
        límites_clase = [min_dato + i * ancho_clase for i in range(num_clases + 1)]
        límites_clase[-1] = max_dato  # Asegurar que el último límite es el valor máximo
        return límites_clase

    def calcular_puntos_medios(self, límites_clase):
        puntos_medios = [(límites_clase[i] + límites_clase[i + 1]) / 2 for i in range(len(límites_clase) - 1)]
        return puntos_medios
