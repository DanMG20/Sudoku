import sys 
import os

def resource_path(relative_path): 
    try:
        # PyInstaller crea una carpeta temporal y la guarda aquí
        base_path = sys._MEIPASS
    except AttributeError:
        # Cuando corres en modo normal
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)