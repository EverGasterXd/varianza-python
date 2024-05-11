import pandas as pd

class CrearTabla:
    def __init__(self, datos):
        self.datos = datos
        self.num_datos = len(datos)
        
    def calcular_tabla(self, num_clases=None):
        if num_clases is None:
            # Calcular el número de clases utilizando la regla de Scott
            ancho_banda = 3.5 * self.std() / (self.num_datos ** (1/2))
            num_clases = int((max(self.datos) - min(self.datos)) / ancho_banda)
        
        # Calcular los límites de clase
        límites_clase = self.calcular_límites_clase(num_clases)
        
        # Calcular las frecuencias absolutas
        frecuencias_absolutas = pd.cut(self.datos, límites_clase, include_lowest=True).value_counts().sort_index().tolist()
        
        # Calcular frecuencia relativa
        frecuencia_relativa = [f / self.num_datos for f in frecuencias_absolutas]
        
        # Calcular frecuencia acumulada
        frecuencia_acumulada = pd.Series(frecuencias_absolutas).cumsum().tolist()
        
        # Calcular frecuencia relativa acumulada
        frecuencia_relativa_acumulada = pd.Series(frecuencia_relativa).cumsum().tolist()
        
        # Calcular el punto medio de cada clase
        puntos_medios = self.calcular_puntos_medios(límites_clase)
        
        # Crear DataFrame para la tabla de frecuencia
        tabla = pd.DataFrame({
            'Clases': [f"{límites_clase[i]} - {límites_clase[i+1]}" for i in range(len(límites_clase) - 1)],
            'xi': puntos_medios,
            'Frecuencia absoluta': frecuencias_absolutas,
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
        límites_clase = [min_dato + i * ancho_clase for i in range(num_clases)]
        límites_clase.append(max_dato)
        return límites_clase

    def calcular_puntos_medios(self, límites_clase):
        return [(límites_clase[i] + límites_clase[i+1]) / 2 for i in range(len(límites_clase) - 1)]
    
    def calcular_media(self):
        suma_xi_fi = sum(self.datos['Punto medio'] * self.datos['Frecuencia absoluta'])
        suma_fi = sum(self.datos['Frecuencia absoluta'])
        media = suma_xi_fi / suma_fi
        return media
    
    def calcular_varianza(self):
        if 'Punto medio' not in self.datos or 'Frecuencia absoluta' not in self.datos:
            raise ValueError("Las columnas 'Punto medio' y/o 'Frecuencia absoluta' no existen en los datos.")
        
        if not all(isinstance(x, (int, float)) for x in self.datos['Punto medio']):
            raise ValueError("La columna 'Punto medio' debe contener solo números.")
        
        if not all(isinstance(x, (int, float)) for x in self.datos['Frecuencia absoluta']):
            raise ValueError("La columna 'Frecuencia absoluta' debe contener solo números.")
        
        media = self.calcular_media()
        suma = sum((xi - media) ** 2 * fi for xi, fi in zip(self.datos['Punto medio'], self.datos['Frecuencia absoluta']))
        varianza = suma / sum(self.datos['Frecuencia absoluta'])
        return varianza
