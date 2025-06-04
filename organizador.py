# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 12:39:56 2025

@author: DURAN
"""

import os
import shutil

# 1. Ruta de la carpeta que quieres organizar (por defecto: Descargas)
descargas = os.path.expanduser("~/Downloads")  # Cambia esto si quieres otra carpeta

# 2. Diccionario de tipos de archivos agrupados por categoría
tipos = {
    "Imagenes": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".ico"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".odt", ".csv", ".md"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm", ".mpeg", ".3gp"],
    "Musica": [".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a", ".wma"],
    "ZIPs": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "Instaladores": [".exe", ".dmg", ".pkg", ".msi", ".deb", ".rpm", ".apk"],
    "Imagenes-ISO": [".iso", ".img", ".bin", ".nrg"],
    "Automatas": [".jff"],
    "Scripts": [".py", ".js", ".ts", ".sh", ".bat", ".ps1", ".rb", ".pl", ".java", ".c", ".cpp"],
    "BasesDatos": [".sql", ".db", ".sqlite", ".mdb", ".accdb"],
    "Modelos3D": [".stl", ".obj", ".blend", ".fbx", ".dae", ".3ds"],
    "Fuentes": [".ttf", ".otf", ".woff", ".woff2"],
    "Libros": [".epub", ".mobi", ".azw3"],
    "PDF Escaneado": [".pdf"],  # puedes personalizar carpetas duplicadas si usas condiciones más finas
    "Proyectos Web": [".html", ".css", ".scss", ".json", ".xml", ".php"],
    "Apps Móviles": [".apk", ".aab", ".ipa"],
    "Otros": []  # Para archivos sin extensión o no clasificados
}

# 3. Recorremos cada archivo en la carpeta
for archivo in os.listdir(descargas):
    ruta_archivo = os.path.join(descargas, archivo)

    if os.path.isfile(ruta_archivo):
        _, ext = os.path.splitext(archivo)
        ext = ext.lower()

        movido = False
        for carpeta, extensiones in tipos.items():
            if ext in extensiones:
                destino = os.path.join(descargas, carpeta)
                os.makedirs(destino, exist_ok=True)
                shutil.move(ruta_archivo, os.path.join(destino, archivo))
                print(f"✅ Moved: {archivo} → {carpeta}/")
                movido = True
                break

        if not movido:
            # Si la extensión no está en la lista, lo mandamos a "Otros"
            destino = os.path.join(descargas, "Otros")
            os.makedirs(destino, exist_ok=True)
            shutil.move(ruta_archivo, os.path.join(destino, archivo))
            print(f"📁 Moved to 'Otros': {archivo}")
