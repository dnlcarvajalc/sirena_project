import os
import json
from datetime import datetime


def save_dates(message):
    """ Esta función crea una estructura de carpetas nombradas con la información de
        la fecha actual en el orden de año, mes y día (YYYY/MM/DD).
        Además genera un archivo de texto plano nombrado con la hora actual en
        el orden de hora, minuto y segundo (hh_mm_ss.json) que contiene información.

    Args:
        message (str): Contiene la información del lugar que haya sido consultado.
    """
    #Fecha y hora actual
    current_date_and_time = datetime.now()
    YYYY = current_date_and_time.strftime("%Y")
    MM = current_date_and_time.strftime("%m")
    DD = current_date_and_time.strftime("%j")
    hh = current_date_and_time.strftime("%H")
    mm = current_date_and_time.strftime("%M")
    ss = current_date_and_time.strftime("%S")

    #Crear archivo hh_mm_ss.json
    file_name_js = hh + '_' + mm + '_' + ss + '.json'
    if message is not None:
        data_js = message
    else:
        data_js = {'hh': hh , 'mm': mm , 'ss': ss}

    #Obtener ruta de la carpeta actual
    folder_path = os.path.abspath(os.getcwd())
    #Crear la ruta '/YYYY/MM/DD' en la carpeta actual
    os.makedirs(folder_path + '/' + str(YYYY) + '/' + str(MM) + '/' + str(int(DD)), exist_ok=True)

    #Guardar archivo hh_mm_ss.json en la ruta creada
    with open(os.path.join(folder_path +  '/' + str(YYYY) + '/' + str(MM) + '/' + str(int(DD)), file_name_js), 'w') as file:
        json.dump(data_js, file)

save_dates("Prueba")
