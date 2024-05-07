import math
from tabulate import tabulate
import agrupados
import noAgrupados

print("""
escoge cual quieres usar
 1.- no agrupados
 2.- agrupados
 """)
opciones = int(input())
if opciones == 1:
    
    datos = input("Ingresa números separados por espacios:\n")
    numeros = [int(d) for d in datos.split() if d.isdigit()]
    
    if len(numeros) >=30:
            print("pasaste la cantidad numeros posibles")
            exit()
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
        
if opciones == 2:
    datos = input("Ingresa números separados por espacios:\n")

    numeros = [int(d) for d in datos.split() if d.isdigit()]

    # if len(numeros) > 31:
    #     print("Pasaste la cantidad máxima de números posibles")
    #     exit()


    tabla, xi, intervalo, clases = agrupados.crearTabla(numeros)
    headers = ["Clase", "Punto Medio (xi)", "Frecuencia", "Frecuencia Relativa", "Frecuencia Acumulada", "Frecuencia Acumulada Relativa"]
    # Formatear tabla usando tabulate
    tabla_formateada = []
    for i, (dato, info) in enumerate(tabla.items()):
        # Verificar si el índice i está dentro del rango válido de la lista xi
        if isinstance(xi, list) and i < len(xi) - 1:
            tabla_formateada.append([f"{xi[i]} - {xi[i + 1]}" , info["frecuencia"], info["frecuencia relativa"], info["frecuencia acumulada"], info["frecuencia acumulada relativa"]])
        else:
            # Manejar el caso en que el índice i está fuera de rango
            print(f"¡Advertencia! Índice i ({i}) fuera de rango para la clase {dato}")

    # Imprimir tabla formateada
    print(tabulate(tabla_formateada, headers=headers, tablefmt="grid"))

    print("Media:", agrupados.media(tabla))
    print("clases: ", clases)
    print("cantidad: ", len(numeros))
    print("Mediana:", agrupados.mediana(tabla, intervalo))
    print("Moda:", agrupados.moda(tabla))
    print("Varianza:", agrupados.varianza(tabla))
    print("Desviación Estándar:", agrupados.d_e(tabla))

        




input("Presione Enter para cerrar el programa.")
