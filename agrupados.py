import math
from collections import Counter

class CrearTabla:
    def __init__(self, datos):
        self.datos = datos
        self.num_datos = len(datos) - 1  # Restamos 1 a la cantidad de datos

    def calcular_tabla(self, num_clases=None):
        if num_clases is None:
            num_clases = math.ceil(1 + math.log2(self.num_datos))

        limites_clase = self.calcular_limites_clase(num_clases)
        frecuencias_absolutas = self.calcular_frecuencias_absolutas(limites_clase)
        frecuencia_relativa = [round(f / self.num_datos, 2) for f in frecuencias_absolutas]
        frecuencia_acumulada = [sum(frecuencias_absolutas[:i + 1]) for i in range(len(frecuencias_absolutas))]
        frecuencia_relativa_acumulada = [round(sum(frecuencia_relativa[:i + 1]), 2) for i in range(len(frecuencia_relativa))]
        puntos_medios = self.calcular_puntos_medios(limites_clase)

        tabla = []
        for i in range(len(limites_clase) - 1):
            tabla.append([
                f"{round(limites_clase[i], 2)} - {round(limites_clase[i + 1], 2)}",
                round(puntos_medios[i], 2),
                frecuencias_absolutas[i],
                frecuencia_relativa[i],
                frecuencia_acumulada[i],
                frecuencia_relativa_acumulada[i]
            ])

        return tabla

    def calcular_media(self):
        media = round(sum(self.datos) / self.num_datos, 2)
        return media

    def calcular_mediana(self):
        datos_ordenados = sorted(self.datos)
        mitad = self.num_datos // 2
        if self.num_datos % 2 == 0:
            mediana = (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
        else:
            mediana = datos_ordenados[mitad]
        return round(mediana, 2)

    def calcular_moda(self):
        tabla = self.calcular_tabla()
        frecuencias = [fila[2] for fila in tabla]
        max_frecuencia = max(frecuencias)
        i = frecuencias.index(max_frecuencia)

        # Variables necesarias
        limiteInferior = float(tabla[i][0].split()[0])
        frecuenciaModal = frecuencias[i]
        frecuenciaModalAnterior = frecuencias[i - 1] if i > 0 else 0
        frecuenciaModalSiguiente = frecuencias[i + 1] if i < len(frecuencias) - 1 else 0
        A = float(tabla[0][0].split('-')[1]) - float(tabla[0][0].split('-')[0]) 

        # Cálculo de la moda utilizando la fórmula proporcionada
        moda = limiteInferior + ((frecuenciaModal - frecuenciaModalAnterior) / ((frecuenciaModal - frecuenciaModalAnterior) + (frecuenciaModal - frecuenciaModalSiguiente))) * A
        return round(moda, 2)

    def calcular_varianza(self):
        media = self.calcular_media()
        varianza = sum((x - media) ** 2 for x in self.datos) / self.num_datos
        return round(varianza, 2)

    def calcular_desviacion_estandar(self):
        varianza = self.calcular_varianza()
        desviacion_estandar = math.sqrt(varianza)
        return round(desviacion_estandar, 2)

    def calcular_limites_clase(self, num_clases):
        min_dato = min(self.datos)
        max_dato = max(self.datos)
        ancho_clase = (max_dato - min_dato) / num_clases
        limites_clase = [min_dato + i * ancho_clase for i in range(num_clases + 1)]
        limites_clase[-1] = max_dato  # Aseguramos que el último límite sea exactamente el máximo valor del dato
        return limites_clase

    def calcular_frecuencias_absolutas(self, limites_clase):
        frecuencias = [0] * (len(limites_clase) - 1)
        for dato in self.datos:
            for i in range(len(limites_clase) - 1):
                if limites_clase[i] <= dato < limites_clase[i + 1]:
                    frecuencias[i] += 1
                    break
        # Aseguramos que el último dato se incluya en la última clase
        if self.datos[-1] == limites_clase[-1]:
            frecuencias[-1] += 1
        return frecuencias

    def calcular_puntos_medios(self, limites_clase):
        puntos_medios = [(limites_clase[i] + limites_clase[i + 1]) / 2 for i in range(len(limites_clase) - 1)]
        return puntos_medios
