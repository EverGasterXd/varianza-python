import math

def media(numeros):
    return sum(numeros) / len(numeros)


def mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 0:
        return (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
    else:
        return numeros_ordenados[n//2]

def moda(numeros):
    count = {}
    for num in numeros:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    moda_frecuencia = max(count.values())
    modas = [num for num, freq in count.items() if freq == moda_frecuencia]
    return modas


def tabla(x):
    tabla = {}
    totalDatos = len(x)

    minimo = min(x)
    maximo = max(x)
    rango = maximo - minimo
    for dato in x:
        if dato in tabla:
            tabla[dato]["frecuencia"] += 1
        else:
            tabla[dato] = {"frecuencia": 1}
    
    frecuenciaAcumulada = 0
    for dato, info in tabla.items():
        frecuencia = info["frecuencia"]
        frecuenciarelativa = frecuencia / totalDatos
        frecuenciaAcumulada += frecuencia
        frecuenciaAcumuladarelativa = frecuenciaAcumulada / totalDatos

        info["frecuencia relativa"] = frecuenciarelativa
        info["frecuencia acumulada"] = frecuenciaAcumulada
        info["frecuencia acumulada relativa"] = frecuenciaAcumuladarelativa
    
    return tabla, rango


def varianza(xq):
    mean = media(xq)
    return math.fsum([math.pow((x - mean), 2) for x in xq]) / len(xq)


def d_e(xq):
    return math.sqrt(varianza(xq))