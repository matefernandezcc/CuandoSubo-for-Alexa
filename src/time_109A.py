import os
import sys
import requests
from bs4 import BeautifulSoup
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from utils.utils import restar_tiempo, enviar_Alexa

# URL de la página web del 109A
url = 'https://cuandosubo.sube.gob.ar/onebusaway-webapp/where/iphone/stop.action?id=82_201807&route=24_287'
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    
    # Parsear el HTML de la página web
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar el elemento <div> con la clase "arrivalsStatusUpdates"
    update_element = soup.find('div', class_='arrivalsStatusUpdates')
    last_update = update_element.text.strip().split(': ')[1]  # Extraer el texto del último update
    
    print(f"\n\t===== Última actualización: {last_update} =====")
    
    # Encontrar todos los elementos <tr> con la clase "arrivalsRow"
    arrivals_rows = soup.find_all('tr', class_='arrivalsRow')
    
    # Iterar sobre los elementos encontrados
    for row in arrivals_rows:
        # Encontrar el elemento <td> que contiene la ruta del autobús
        route_element = row.find('td', class_='arrivalsRouteEntry')
        route = route_element.text.strip()  # Extraer el texto de la ruta
        
        # Verificar si la ruta coincide con "145C"
        if route == "109A" or route == "109C":
            # Encontrar el elemento <span> que contiene el horario de llegada
            time_element = row.find('span', class_='arrivalsTimeEntry')
            arrival_time = time_element.text.strip()  # Extraer el texto del horario de llegada
            
            print(f"Horario de llegada del 145C a la parada 378 PATRICIAS ARGENTINAS AV: {arrival_time}\n")
            enviar_Alexa(restar_tiempo(arrival_time, 0))
else:
    print(f"Error al cargar la página: {response.status_code}")