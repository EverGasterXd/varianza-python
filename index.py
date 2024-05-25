import os
from tabulate import tabulate
import agrupados
import noAgrupados

def solicitar_nombre_archivo():
    while True:
        nombre_archivo = input("Ingresa el nombre del archivo para guardar la información (sin extensión): ") + '.txt'
        if os.path.exists(nombre_archivo):
            print(f"El archivo '{nombre_archivo}' ya existe. Por favor, ingresa un nuevo nombre.")

            if os.path.exists(nombre_archivo):
                eleccion = input("quieres sobre escribir el archivo? (s/n): ")
                if eleccion =='s':
                    return nombre_archivo
        else:
            return nombre_archivo

def main():

    while(True):
        try:
            print("""
            1.- datos agrupados/noagrupados
            2.- consultar tabla de archivo
            3.- salir""")
            opc = int(input("escoge una opcion: "))
            if opc == 1:
                datos = input("Ingresa números separados por espacios:\n")
                numeros = [float(d) for d in datos.split() if d.replace('.', '', 1).isdigit()]
                numeros.sort()

                if len(numeros) <= 1:
                    print("No puedes hacer con esto una tabla")
                    exit()

                if len(numeros) <= 29:
                    tabla, rango = noAgrupados.tabla(numeros)
                    headers = ["Dato", "Frecuencia", "Frecuencia relativa", "Frecuencia acumulada", "frecuencia acumulada relativa"]
                    no_agrupados = []
                    for dato, info in tabla.items():
                        no_agrupados.append([dato, info["frecuencia"], info["frecuencia relativa"], info["frecuencia acumulada"], info["frecuencia acumulada relativa"]])

                    print(tabulate(no_agrupados, headers=headers, tablefmt="psq1"))
                    print(f"""
                    Los números ingresados son: {", ".join(map(str, numeros))}
                    Rango: {rango}
                    Varianza: {noAgrupados.varianza(numeros)}
                    Media: {noAgrupados.media(numeros)}
                    Mediana: {noAgrupados.mediana(numeros)}
                    Moda: {noAgrupados.moda(numeros)}
                    Desviación estándar: {noAgrupados.d_e(numeros)}
                    """)

                    
                    nombre_archivo = solicitar_nombre_archivo()
                    with open(nombre_archivo, 'w') as f:
                        f.write(tabulate(no_agrupados, headers=headers, tablefmt="psq1"))
                        f.write(f"""
                        Los números ingresados son: {", ".join(map(str, numeros))}
                        Rango: {rango}
                        Varianza: {noAgrupados.varianza(numeros)}
                        Media: {noAgrupados.media(numeros)}
                        Mediana: {noAgrupados.mediana(numeros)}
                        Moda: {noAgrupados.moda(numeros)}
                        Desviación estándar: {noAgrupados.d_e(numeros)}
                        """)
                        
                    print(f"La información se ha guardado en '{nombre_archivo}'")
                    os.startfile(nombre_archivo)

                    input("presione Enter para continuar")
                    os.system('cls')
                else:
                    tabla = agrupados.CrearTabla(numeros)
                    headers = ["Clases", "xi", "Frecuencia absoluta", "Frecuencia relativa", "Frecuencia acumulada", "Frecuencia relativa acumulada"]
                    tabla_frecuencia = tabla.calcular_tabla()

                    print(tabulate(tabla_frecuencia, headers=headers, tablefmt='psq1'))
                    print(f"""
                    Los numeros ingresados son: {", ".join(map(str, numeros))}
                    Varianza: {tabla.calcular_varianza()}
                    Media: {tabla.calcular_media()}
                    Mediana: {tabla.calcular_mediana()}
                    Moda: {tabla.calcular_moda()}
                    Desviacion estandar: {tabla.calcular_desviacion_estandar()}
                    """)

                    nombre_archivo = solicitar_nombre_archivo()
                    with open(nombre_archivo, 'w') as f:
                        f.write(tabulate(tabla_frecuencia, headers=headers, tablefmt='psq1'))
                        f.write(f"""
                        Los numeros ingresados son: {", ".join(map(str, numeros))}
                        Varianza: {tabla.calcular_varianza()}
                        Media: {tabla.calcular_media()}
                        Mediana: {tabla.calcular_mediana()}
                        Moda: {tabla.calcular_moda()}
                        Desviacion estandar: {tabla.calcular_desviacion_estandar()}
                        """)
                    print(f"La información se ha guardado en '{nombre_archivo}'")
                    os.startfile(nombre_archivo)

                    input("Presione Enter para continuar.")
                    os.system('cls')

            elif opc == 2:
                nombre = input("ingresa el nombre del archivo (sin extension): ") + ".txt"
                if not os.path.exists(nombre):
                    print("este archivo no existe")
                    input("presione Enter para continuar")
                    os.system('cls')
                
                else:
                    x = open(nombre)
                    print(x.read())
                    input("presione Enter para continuar")
                    os.system('cls')

            elif opc == 3:
                print("Gracias por usar el programa")
                os.system('cls')
                exit()
        except ValueError:
            print("hay un error")
            input("presione Enter para continuar")
            os.system('cls')

if __name__ == "__main__":
    main()
