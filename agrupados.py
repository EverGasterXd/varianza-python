import math
def crearTabla(x):
    tabla = {}
    totalDatos = len(x)


    minimo = min(x)
    maximo = max(x)
    rango = maximo - minimo

    # Calcular el número de clases redondeando según las especificaciones

    clases = math.ceil(1 + 3.322 * math.log(totalDatos, 10))

    limite = clases

    # Calcular el intervalo
    intervalo = rango / limite

    frecuenciaAcumulada = 0
    xi = []
    # Calcular los puntos medios xi
    limite_inferior = minimo
    for i in range(limite):
        limite_superior = round(limite_inferior + intervalo, 1)
        for dato in x:
            if limite_inferior <= round(dato, 1) < math.ceil(limite_superior):
                if dato in tabla:
                    tabla[dato]["frecuencia"] += 1
                else:
                    tabla[dato] = {"frecuencia": 1}

        punto_medio = round(limite_inferior + (intervalo), 1)
        xi.append(punto_medio)
        limite_inferior = limite_superior


    for info in tabla.values():
        frecuencia = info["frecuencia"]
        frecuenciarelativa = frecuencia / totalDatos
        frecuenciaAcumulada += frecuencia
        frecuenciaAcumuladarelativa = frecuenciaAcumulada / totalDatos

        info["frecuencia relativa"] = frecuenciarelativa
        info["frecuencia acumulada"] = frecuenciaAcumulada
        info["frecuencia acumulada relativa"] = frecuenciaAcumuladarelativa

    return tabla, xi, intervalo, clases


def media(datos_agrupados):
    suma = 0
    total_frecuencia = 0
    for xi, info in datos_agrupados.items():
        suma += xi * info["frecuencia"]
        total_frecuencia += info["frecuencia"]
    return suma / total_frecuencia if total_frecuencia != 0 else 0


def mediana(datos_agrupados, intervalo):
    total_frecuencia = sum(info["frecuencia"] for info in datos_agrupados.values())
    mediana_index = total_frecuencia / 2

    # Buscar la clase de la mediana
    frecuencia_acumulada = 0
    for xi, info in datos_agrupados.items():
        frecuencia_acumulada += info["frecuencia"]
        if frecuencia_acumulada >= mediana_index:
            clase_mediana = xi
            break

    # Calcular la mediana
    limite_inferior = clase_mediana - intervalo / 2
    frecuencia_mediana = datos_agrupados[clase_mediana]["frecuencia"]
    mediana = limite_inferior + ((mediana_index - (frecuencia_acumulada - frecuencia_mediana)) / frecuencia_mediana) * intervalo
    return mediana


def moda(datos_agrupados):
    moda_frecuencia = max(info["frecuencia"] for info in datos_agrupados.values())
    modas = [xi for xi, info in datos_agrupados.items() if info["frecuencia"] == moda_frecuencia]
    return modas


def varianza(datos_agrupados):
    media_val = media(datos_agrupados)
    total_frecuencia = sum(info["frecuencia"] for info in datos_agrupados.values())
    suma = sum(((xi - media_val) ** 2) * info["frecuencia"] for xi, info in datos_agrupados.items())
    return suma / total_frecuencia if total_frecuencia != 0 else 0


def d_e(datos_agrupados):
    return math.sqrt(varianza(datos_agrupados))
