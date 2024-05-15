import pandas as pd
import numpy as np

class CrearTabla:
    def __init__(self, datos):
        self.datos = datos
        self.num_datos = len(datos)
        
    def calcular_tabla(self, num_clases=None):
        if num_clases is None:
<<<<<<< HEAD
            ancho_banda = 3.5 * self.datos['xi'].std() / (self.num_datos ** (-1/3))
            num_clases = int(np.ceil((max(self.datos['xi']) - min(self.datos['xi'])) / ancho_banda))
=======
            # Calcular el número de clases utilizando la regla de Scott
            ancho_banda = 3.5 * self.std() / (self.num_datos ** (1/2))
            num_clases = int((max(self.datos) - min(self.datos)) / ancho_banda)
<<<<<<< HEAD
>>>>>>> parent of ac01303 (agrupados)
=======
>>>>>>> parent of ac01303 (agrupados)
        
        límites_clase = self.calcular_límites_clase(num_clases)
<<<<<<< HEAD
        frecuencias_absolutas = pd.cut(self.datos['xi'], límites_clase, include_lowest=True, right=False).value_counts().sort_index().tolist()
        frecuencia_relativa = [round(f / self.num_datos, 4) for f in frecuencias_absolutas]
=======
        
        # Calcular las frecuencias absolutas
        frecuencias_absolutas = pd.cut(self.datos, límites_clase, include_lowest=True).value_counts().sort_index().tolist()
        
        # Calcular frecuencia relativa
        frecuencia_relativa = [f / self.num_datos for f in frecuencias_absolutas]
        
        # Calcular frecuencia acumulada
>>>>>>> parent of ac01303 (agrupados)
        frecuencia_acumulada = pd.Series(frecuencias_absolutas).cumsum().tolist()
        frecuencia_relativa_acumulada = pd.Series(frecuencia_relativa).cumsum().tolist()
        puntos_medios = self.calcular_puntos_medios(límites_clase)
        
        tabla = pd.DataFrame({
            'Clases': [f"{límites_clase[i]} - {límites_clase[i+1]}" for i in range(len(límites_clase) - 1)],
            'xi': puntos_medios,
            'Frecuencia absoluta': frecuencias_absolutas,
            'Frecuencia relativa': frecuencia_relativa,
            'Frecuencia acumulada': frecuencia_acumulada,
            'Frecuencia relativa acumulada': [round(x, 4) for x in frecuencia_relativa_acumulada]
        })
        
        return tabla
<<<<<<< HEAD
<<<<<<< HEAD

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
=======
    
    def std(self):
        mean = sum(self.datos) / self.num_datos
        variance = sum((x - mean) ** 2 for x in self.datos) / self.num_datos
        return variance ** 0.5
    
    def calcular_límites_clase(self, num_clases):
        min_dato = min(self.datos)
        max_dato = max(self.datos)
        ancho_clase = (max_dato - min_dato) / num_clases
        límites_clase = [min_dato + i * ancho_clase for i in range(num_clases)]
        límites_clase.append(max_dato)
        return límites_clase

    def calcular_puntos_medios(self, límites_clase):
=======
    
    def std(self):
        mean = sum(self.datos) / self.num_datos
        variance = sum((x - mean) ** 2 for x in self.datos) / self.num_datos
        return variance ** 0.5
    
    def calcular_límites_clase(self, num_clases):
        min_dato = min(self.datos)
        max_dato = max(self.datos)
        ancho_clase = (max_dato - min_dato) / num_clases
        límites_clase = [min_dato + i * ancho_clase for i in range(num_clases)]
        límites_clase.append(max_dato)
        return límites_clase

    def calcular_puntos_medios(self, límites_clase):
>>>>>>> parent of ac01303 (agrupados)
        return [(límites_clase[i] + límites_clase[i+1]) / 2 for i in range(len(límites_clase) - 1)]
    
    def calcular_media(self):
        suma_xi_fi = sum(self.datos['xi'] * self.datos['Frecuencia absoluta'])
        suma_fi = sum(self.datos['Frecuencia absoluta'])
        media = suma_xi_fi / suma_fi
        return media
    
    def calcular_varianza(self):
        if 'xi' not in self.datos.columns or 'Frecuencia absoluta' not in self.datos.columns:
            raise ValueError("Las columnas 'xi' y/o 'Frecuencia absoluta' no existen en los datos.")
        
        if not all(isinstance(x, (int, float)) for x in self.datos['xi']):
            raise ValueError("La columna 'xi' debe contener solo números.")
        
        if not all(isinstance(x, (int, float)) for x in self.datos['Frecuencia absoluta']):
            raise ValueError("La columna 'Frecuencia absoluta' debe contener solo números.")
        
        media = self.calcular_media()
        suma = sum((xi - media) ** 2 * fi for xi, fi in zip(self.datos['xi'], self.datos['Frecuencia absoluta']))
        varianza = suma / sum(self.datos['Frecuencia absoluta'])
<<<<<<< HEAD
        return varianza
>>>>>>> parent of ac01303 (agrupados)
=======
        return varianza
>>>>>>> parent of ac01303 (agrupados)
