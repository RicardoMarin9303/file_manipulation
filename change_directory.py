#!/usr/bin/env python3
"""
Proyecto que tiene la finalidad de manipular ciertos ficheros bajo el lenguaje de programacion python
"""

# Importamos librerias
import os
# Variables
directory = os.getcwd()
# Declaramos nuestra funcion
def change_name(directory, signo):
# lista todo los ficheros y directorios
    for i in os.listdir(directory):
# Si es un directorio, continua
        if os.path.isdir(i):
# almacenamos en un string nuestro nombre
            replace_name = i.replace(" ", signo)
            path_name = os.path.join(directory, i)
            path_replace = os.path.join(directory, replace_name)
            os.rename(path_name, path_replace)
        else:
            print("En el siguiente fichero, " + i + " tienes un error")
            print("")


# inicializamos la funcion
change_name(directory, "_")
