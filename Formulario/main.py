import mysql.connector
import csv
import os
import json
from clases.recursos import recurso
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="pis_iiidb"
)
c = mydb.cursor()
c.execute("SHOW DATABASES")
# for i in c:
#     print(i)
# c = mydb.cursor()
# mydb.close()

def print_opcion():
    print({"GESTOR DE CONTENIDO\n",          
           "Opciones:\n ",
           "1. Crear nuevo recurso\n",
           "2. Buscar recurso\n ",
           "3. Modificar recurso\n",
           "4. Eliminar recurso\n"
           "5. Salir"
           })
def crear_recurso(recurso_id):
    print("Crear recurso \n")
    #fecha=int()
    tipo_recurso=input("Ingrese el tipo de recurso: \n")
    recurso_nuevo = {
        #'id': str(recurso_id),
        'Tipo de recurso':tipo_recurso,
        # 'Descripcion': nombre,
        # 'Imagen': apellido,
        # 'Recurso ': recurso
        # 'Link':
        # 'Fecha': str(fecha)
    }
    
    mydb.info.insert_one(recurso_nuevo)
    print("Recurso creado exitosamente")
def ingresado():
    print_opcion()
    opcion=input("Ingrese acción a realizar: ")
    if opcion == "1":
        pass
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        exit
    else:
        print('Error en la opción seleccionada')
        print_opcion()
    
    if __name__== "__main__":
        ingresado()