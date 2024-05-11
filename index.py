import math
import agrupados
import noAgrupados
from tabulate import tabulate


datos = input("Ingresa números separados por espacios:\n")
numeros = [float(d) for d in datos.split() if d.isdigit()]
    
numeros.sort()
"""
hace la tabla de manera de no agrupados, cuando no es mas de 29 datos
"""
if len(numeros) <= 1:
     print("no puedes hacer con esto una tabla")
     exit()

if len(numeros) <= 29:
        tabla, rango = noAgrupados.tabla(numeros)
        headers = ["Dato", "frecuencia", "frecuencia relativa", "frecuencia acumulada", "frecuencia relativa acumulada"]
        no_agrupados = []
        for i,(dato, info) in enumerate(tabla.items()):
            no_agrupados.append([dato, info["frecuencia"], info["frecuencia relativa"], info["frecuencia acumulada"], info["frecuencia acumulada relativa"]])

        print(tabulate(no_agrupados, headers=headers, tablefmt="psq1"))
        print(f"""
        {"Los números ingresados son:", ", ".join(map(str, numeros))}
        rango: {rango}
        varianza: {noAgrupados.varianza(numeros)}
        media: {noAgrupados.media(numeros)}
        mediana: {noAgrupados.mediana(numeros)}
        moda: {noAgrupados.moda(numeros)}
        desviacion estandar: {noAgrupados.d_e(numeros)}""")

        guardar = input("¿Quieres guardar esta información en un archivo de texto? (s/n): ")
        if guardar.lower() == 's':
            with open('resultados.txt', 'w') as f:
                f.write(tabulate(no_agrupados, headers=headers, tablefmt="psq1"))
                f.write(f"""
                {"Los numeros ingresados son:", ", ".join(map(str, numeros))}
                rango: {rango}
                varianza: {noAgrupados.varianza(numeros)}
                media: {noAgrupados.media(numeros)}
                mediana: {noAgrupados.mediana(numeros)}
                moda: {noAgrupados.moda(numeros)}
                """)
            print("La información se ha guardado en 'resultados.txt'")
        else:
             print("cerrando programa")
             exit()
             
else:
    tabla = agrupados.CrearTabla(numeros)
    headers = ["frecuencia(xi)", "frecuencia relativa", "frecuencia acumulada", "frecuencia relativa acumulada"]
    tabla_frecuencia = tabla.calcular_tabla()
    varianza = tabla.calcular_varianza()
    media = tabla.calcular_media()
    print(tabulate(tabla_frecuencia, headers=headers, tablefmt='psq1'))
    print(f"""
    {"Los números ingresados son:", ", ".join(map(str, numeros))}
    varianza: {varianza}
    media: {media}
    mediana: aun no lo hago
    """)
        
input("Presione Enter para cerrar el programa.")
