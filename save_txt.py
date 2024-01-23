import os
import json
from os import makedirs
import datetime as dt


def save_dates():
    #Fecha y hora actual
    current_date_and_time = dt.datetime.now()
    yyyy = current_date_and_time.strftime("%Y")
    mm = current_date_and_time.strftime("%m")
    dd = current_date_and_time.strftime("%w")
    hh = current_date_and_time.strftime("%H")
    mm = current_date_and_time.strftime("%M")
    ss = current_date_and_time.strftime("%S")

    #Crear archivo hh_mm_ss.json
    file_name_js = 'hh_mm_ss.json'
    data_js = {'hh': hh , 'mm': mm , 'ss': ss}

    #Obtener ruta de la carpeta actual
    folder_path = os.path.abspath(os.getcwd())
    #Crear la ruta '/YYYY/MM/DD' en la carpeta actual
    os.makedirs(folder_path + '/' + str(yyyy) + '/' + str(mm) + '/' + str(dd), exist_ok=True)

    #Guardar archivo hh_mm_ss.json en la ruta creada
    with open(os.path.join(folder_path +  '/' + str(yyyy) + '/' + str(mm) + '/' + str(dd), file_name_js), 'w') as file:
        json.dump(data_js, file)

save_dates()
