import pandas as pd
import numpy as np

class CrearTabla:
    def __init__(self, datos):
        self.datos = pd.DataFrame({'xi': datos})
        self.num_datos = len(datos)

    def calcular_tabla(self, num_clases=None):
        if num_clases == None:
            # Calcular el número de clases utilizando la Regla de Sturges
            num_clases = int(np.ceil(1 + np.log2(self.num_datos)))

        # Calcular los límites de clase
        límites_clase = self.calcular_límites_clase(num_clases)

        # Calcular las frecuencias absolutas
        frecuencias_absolutas = pd.cut(self.datos['xi'], límites_clase, include_lowest=True, right=False).value_counts().sort_index().tolist()

        # Calcular frecuencia relativa
        frecuencia_relativa = [round(f / self.num_datos, 4) for f in frecuencias_absolutas]

        # Calcular frecuencia acumulada
        frecuencia_acumulada = pd.Series(frecuencias_absolutas).cumsum().tolist()

        # Calcular frecuencia relativa acumulada
        frecuencia_relativa_acumulada = pd.Series(frecuencia_relativa).cumsum().tolist()

        # Calcular el punto medio de cada clase
        puntos_medios = self.calcular_puntos_medios(límites_clase)

        # Crear DataFrame para la tabla de frecuencia
        tabla = pd.DataFrame({
            'Clases': [f"{round(límites_clase[i], 2)} - {round(límites_clase[i+1], 2)}" for i in range(len(límites_clase) - 1)],
            'xi': [round(x, 2) for x in puntos_medios],
            'Frecuencia absoluta': frecuencias_absolutas,
            'Frecuencia relativa': frecuencia_relativa,
            'Frecuencia acumulada': frecuencia_acumulada,
            'Frecuencia relativa acumulada': frecuencia_relativa_acumulada
        })

        return tabla

    def calcular_media(self):
        media = round(self.datos['xi'].mean(), 2)
        return media

    def calcular_mediana(self):
        mediana = round(self.datos['xi'].median(), 2)
        return mediana

    def calcular_moda(self):
        moda = self.datos['xi'].mode()
        if len(moda) > 1:
            return [round(m, 2) for m in moda]
        else:
            return round(moda.iloc[0], 2)

    def calcular_varianza(self):
        varianza = round(self.datos['xi'].var(ddof=0), 2)
        return varianza

    def calcular_desviacion_estandar(self):
        desviacion_estandar = round(self.datos['xi'].std(ddof=0), 2)
        return desviacion_estandar

    def calcular_límites_clase(self, num_clases):
        min_dato = self.datos['xi'].min()
        max_dato = self.datos['xi'].max()
        ancho_clase = (max_dato - min_dato) / num_clases
        límites_clase = [min_dato + i * ancho_clase for i in range(num_clases + 1)]
        # Aseguramos que el último límite sea exactamente el máximo valor del dato
        límites_clase[-1] = max_dato
        return límites_clase

    def calcular_puntos_medios(self, límites_clase):
        puntos_medios = [(límites_clase[i] + límites_clase[i + 1]) / 2 for i in range(len(límites_clase) - 1)]
        return puntos_medios
