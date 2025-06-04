# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 12:39:56 2025

@author: DURAN
"""

import os
import shutil

# 1. Ruta de la carpeta que quieres organizar
descargas = os.path.expanduser("~/Downloads")

# 2. Extensiones agrupadas por tipo siq uiere agregar otro usa esta estructura 
# "nombre de la capeta": [y el nombre despues del punto ejemplo .exe ],
tipos = {
    "Imagenes": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "ZIPs": [".zip", ".rar"],
    "Instaladores": [".exe", ".dmg", ".pkg"],
    "Imagenes-ISO": [".iso"],
}

# 3. Recorremos cada archivo en la carpeta
for archivo in os.listdir(descargas):
    ruta_archivo = os.path.join(descargas, archivo)

    if os.path.isfile(ruta_archivo):
        _, ext = os.path.splitext(archivo)

        for carpeta, extensiones in tipos.items():
            if ext.lower() in extensiones:
                destino = os.path.join(descargas, carpeta)
                os.makedirs(destino, exist_ok=True)
                shutil.move(ruta_archivo, os.path.join(destino, archivo))
                break  # Ya lo movimos, salimos del bucle
