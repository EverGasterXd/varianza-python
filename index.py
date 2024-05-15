import agrupados
<<<<<<< HEAD
=======
import noAgrupados
>>>>>>> parent of ac01303 (agrupados)
from tabulate import tabulate
import os
import noAgrupados  # Asegúrate de tener este módulo disponible

def main():
    datos = input("Ingresa números separados por espacios:\n")
    numeros = [float(d) for d in datos.split() if d.replace('.', '', 1).isdigit()]
    numeros.sort()
    
    if len(numeros) <= 1:
        print("No puedes hacer con esto una tabla")
        return
    
    if len(numeros) <= 29:
        tabla, rango = noAgrupados.tabla(numeros)
        headers = ["Dato", "Frecuencia", "Frecuencia relativa", "Frecuencia acumulada", "Frecuencia relativa acumulada"]
        no_agrupados = [[dato, tabla['frecuencia'][dato], round(tabla['frecuencia relativa'][dato], 4), tabla['frecuencia acumulada'][dato], round(tabla['frecuencia relativa acumulada'][dato], 4)] for dato in tabla['frecuencia'].index]

        print(tabulate(no_agrupados, headers=headers, tablefmt="psql"))
        print(f"""
        Números ingresados: {", ".join(map(str, numeros))}
        Rango: {rango}
        Varianza: {noAgrupados.varianza(numeros)}
        Media: {noAgrupados.media(numeros)}
        Mediana: {noAgrupados.mediana(numeros)}
        Moda: {noAgrupados.moda(numeros)}
        Desviación estándar: {noAgrupados.d_e(numeros)}
        """)

        guardar = input("¿Quieres guardar esta información en un archivo de texto? (s/n): ")
        if guardar.lower() == 's':
            with open('resultados.txt', 'w') as f:
                f.write(tabulate(no_agrupados, headers=headers, tablefmt="psql"))
                f.write(f"""
                Números ingresados: {", ".join(map(str, numeros))}
                Rango: {rango}
                Varianza: {noAgrupados.varianza(numeros)}
                Media: {noAgrupados.media(numeros)}
                Mediana: {noAgrupados.mediana(numeros)}
                Moda: {noAgrupados.moda(numeros)}
                Desviación estándar: {noAgrupados.d_e(numeros)}
                """)
            print("La información se ha guardado en 'resultados.txt'")
            os.startfile('resultados.txt')
        else:
<<<<<<< HEAD
            print("Cerrando programa")

    else:
        tabla = agrupados.CrearTabla(numeros)
        tabla_frecuencia = tabla.calcular_tabla()
        headers = ["Clases", "xi", "Frecuencia absoluta", "Frecuencia relativa", "Frecuencia acumulada", "Frecuencia relativa acumulada"]

        print(tabulate(tabla_frecuencia, headers=headers, tablefmt='psql'))
        print(f"""
        Números ingresados: {", ".join(map(str, numeros))}
        Varianza: {tabla.calcular_varianza()}
        Media: {tabla.calcular_media()}
        Mediana: {tabla.calcular_mediana()}
        Moda: {tabla.calcular_moda()}
        Desviación estándar: {tabla.calcular_desviacion_estandar()}
        """)

        guardar = input("¿Quieres guardar esta información en un archivo de texto? (s/n): ")
        if guardar.lower() == 's':
            with open('resultados.txt', 'w') as f:
                f.write(tabulate(tabla_frecuencia, headers=headers, tablefmt='psql'))
                f.write(f"""
                Números ingresados: {", ".join(map(str, numeros))}
                Varianza: {tabla.calcular_varianza()}
                Media: {tabla.calcular_media()}
                Mediana: {tabla.calcular_mediana()}
                Moda: {tabla.calcular_moda()}
                Desviación estándar: {tabla.calcular_desviacion_estandar()}
                """)
            print("La información se ha guardado en 'resultados.txt'")
            os.startfile('resultados.txt')
        else:
            print("Cerrando programa")

if __name__ == "__main__":
    main()
=======
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
>>>>>>> parent of ac01303 (agrupados)
