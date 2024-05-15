import pandas as pd

class CrearTabla:
    def __init__(self, datos):
        self.datos = datos
        self.num_datos = len(datos)
        
    def calcular_tabla(self, num_clases=None):
        if num_clases is None:
<<<<<<< HEAD
            ancho_banda = 3.5 * self.std() / (self.num_datos ** (1/3))
            num_clases = int((max(self.datos) - min(self.datos)) / ancho_banda)
        
        límites_clase = self.calcular_límites_clase(num_clases)
        
        # Calcular las frecuencias absolutas
        frecuencias_absolutas = pd.cut(self.datos, límites_clase, include_lowest=True).value_counts().sort_index().tolist()
        
        # Calcular frecuencia relativa
        frecuencia_relativa = [f / self.num_datos for f in frecuencias_absolutas]
        
        # Calcular frecuencia acumulada
        frecuencia_acumulada = pd.Series(frecuencias_absolutas).cumsum().tolist()
        frecuencia_relativa_acumulada = pd.Series(frecuencia_relativa).cumsum().tolist()
        puntos_medios = self.calcular_puntos_medios(límites_clase)
        
        tabla = pd.DataFrame({
            'Clases': [f"{round(límites_clase[i], 2)} - {round(límites_clase[i+1], 2)}" for i in range(len(límites_clase) - 1)],
            'xi': puntos_medios,
=======
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
>>>>>>> parent of 94f90c4 (arreglos)
            'Frecuencia absoluta': frecuencias_absolutas,
            'Frecuencia relativa': frecuencia_relativa,
            'Frecuencia acumulada': frecuencia_acumulada,
            'Frecuencia relativa acumulada': [round(x, 4) for x in frecuencia_relativa_acumulada]
        })
        
        return tabla

<<<<<<< HEAD
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
        return [(límites_clase[i] + límites_clase[i+1]) / 2 for i in range(len(límites_clase) - 1)]
    
    def calcular_media(self, tabla):
        suma_xi_fi = sum(tabla['xi'] * tabla['Frecuencia absoluta'])
        suma_fi = sum(tabla['Frecuencia absoluta'])
        media = suma_xi_fi / suma_fi
        return media
    
    def calcular_varianza(self, tabla):
        if 'xi' not in tabla.columns or 'Frecuencia absoluta' not in tabla.columns:
            raise ValueError("Las columnas 'xi' y/o 'Frecuencia absoluta' no existen en los datos.")
        
        if not all(isinstance(x, (int, float)) for x in tabla['xi']):
            raise ValueError("La columna 'xi' debe contener solo números.")
        
        if not all(isinstance(x, (int, float)) for x in tabla['Frecuencia absoluta']):
            raise ValueError("La columna 'Frecuencia absoluta' debe contener solo números.")
        
        media = self.calcular_media(tabla)
        suma = sum((xi - media) ** 2 * fi for xi, fi in zip(tabla['xi'], tabla['Frecuencia absoluta']))
        varianza = suma / sum(tabla['Frecuencia absoluta'])
        return varianza
=======
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
>>>>>>> parent of 94f90c4 (arreglos)
