# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv
from os import path


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    archivo = open('stock.csv')
    data = list(csv.DictReader(archivo))
    for row in data :
            print(row['tornillos'])
            tornillos = 0
    for i in data:
            tornillos += int(i['tornillos'])
    
    print('stock acumulado":', tornillos)
   

    

     
    
    
    

    
    


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    archivo = open('propiedades.csv')
    data = list(csv.DictReader(archivo))
    archivo.close()

    with open('propiedades.csv')as csvfile:
        data= list(csv.DictReader(csvfile))
        lista = []
    for i in data:
        try:
            lista.append(i['ambientes'])
        except:
            continue
    
    cantidad_2_amb = lista.count('2')
    cantidad_3_amb = lista.count('3')   

    print(' 2 ambientes:', cantidad_2_amb)
    print(' 3 ambientes:', cantidad_3_amb)
    
    
        
   
       

    
        
        
    
    
     


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej3()
    #ej4()
