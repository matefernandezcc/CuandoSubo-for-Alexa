import os
from datetime import datetime, timedelta

def url_colectivo(colectivo):
    url = f"https://cuandosubo.sube.gob.ar/onebusaway-webapp/where/iphone/routes.action?query={colectivo}"
    print(url)
    return url

def enviar_Alexa(result):
    os.system(os.environ['USERPROFILE'] + "\\.TRIGGERcmdData\\SendResult.bat "+str(result))

def restar_tiempo(horario, tiempo_a_restar):
    # Obtener el tiempo actual
    tiempo_actual = datetime.now().strftime('%H:%M')
    
    # Convertir el horario de cadena a objeto datetime
    horario_dt = datetime.strptime(horario, '%H:%M')
    
    # Calcular la diferencia de tiempo a restar
    tiempo_delta = timedelta(minutes=tiempo_a_restar)
    
    # Restar el tiempo especificado
    nuevo_horario_dt = horario_dt - tiempo_delta
    
    # Verificar si el nuevo horario es menor que el tiempo actual
    if nuevo_horario_dt < datetime.strptime(tiempo_actual, '%H:%M'):
        # Si el nuevo horario es menor que el tiempo actual, devolver el horario sin restar nada
        return horario
    else:
        nuevo_horario_str = nuevo_horario_dt.strftime('%H:%M')
        return nuevo_horario_str