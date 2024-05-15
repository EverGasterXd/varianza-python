import math
import agrupados
import noAgrupados
from tabulate import tabulate

datos = input("Ingresa números separados por espacios:\n")
numeros = [int(d) for d in datos.split() if d.isdigit()]
    
"""
hace la tabla de manera de no agrupados, cuando no es mas de 29 datos
"""

if len(numeros) <= 29:
        tabla, rango = noAgrupados.tabla(numeros)
        headers = ["Dato", "frecuencia", "frecuencia relativa", "frecuencia acumulada", "frecuencia relativa acumulada"]
        no_agrupados = []
        for i,(dato, info) in enumerate(tabla.items()):
            no_agrupados.append([dato, info["frecuencia"], info["frecuencia relativa"], info["frecuencia acumulada"], info["frecuencia acumulada relativa"]])

        print(tabulate(no_agrupados, headers=headers, tablefmt="grid"))
        print(f"""
        {"Los números ingresados son:", ", ".join(map(str, numeros))}
        rango: {rango}
        varianza: {noAgrupados.varianza(numeros)}
        media: {noAgrupados.media(numeros)}
        mediana: {noAgrupados.mediana(numeros)}
        moda: {noAgrupados.moda(numeros)}
        desviacion estandar: {noAgrupados.d_e(numeros)}""")
else:
    tabla = agrupados.CrearTabla(numeros)

    tabla_frecuencia = tabla.calcular_tabla()

    print(tabulate(tabla_frecuencia, headers='key', tablefmt='grid'))
        




input("Presione Enter para cerrar el programa.")
