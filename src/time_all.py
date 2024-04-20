import os
import sys
import requests
from bs4 import BeautifulSoup
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from utils.utils import restar_tiempo, enviar_Alexa, url_colectivo


def main():
    # Verificar si se proporcionó al menos un parámetro
    if len(sys.argv) > 1:
        colectivo = sys.argv[1]
    else:
        enviar_Alexa("No ingresaste el colectivo")
        print("\nNo ingresaste el colectivo\n")
        sys.exit()

    # Obtener la URL del colectivo
    url = url_colectivo(colectivo)
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Parsear el HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todos los elementos <a> dentro del elemento <ul> con la clase "buttons"
        enlaces = soup.find('ul', class_='buttons').find_all('a')

        # Inicializar una lista para almacenar los textos de cada enlace
        textos_enlaces = []

        # Iterar sobre los enlaces y extraer el texto de cada uno
        for enlace in enlaces:
            textos_enlaces.append(enlace.get_text())

        # Imprimir la lista de textos de los enlaces
        enviar_Alexa(f"Elegir un ramal, ramal 1 {textos_enlaces[0]} o ramal 2 {textos_enlaces[1]}")
    else:
        print(f"Error al realizar la solicitud: {response.status_code}")

if __name__ == "__main__":
    main()
