import os
import pathlib

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def get_image(image):
    # Obtener la ruta absoluta de una imagen.
    # La librería os ya se encarga de lidiar con el sistema 
    # operativo con la función join.
    return os.path.join(CURRENT_DIR, 'src', 'img', image)
