import boto3
import constants
import os
import json

from datetime import datetime

def upload_folder_s3(message):
    """ Esta función crea una estructura de carpetas nombradas con la información de
        la fecha actual en el orden de año, mes y día (YYYY/MM/DD).
        Además genera un archivo de texto plano nombrado con la hora actual en
        el orden de hora, minuto y segundo (hh_mm_ss.json) que contiene información.
        Dicha información se guarda tanto en el local como en el bucket de S3.

    Args:
        message (_type_): Contiene la información del lugar que haya sido consultado.
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

    #Obtener ruta de la carpeta local actual
    folder_path = os.path.abspath(os.getcwd())

    #Crear la ruta '/YYYY/MM/DD' en la carpeta local actual
    os.makedirs(folder_path + '/' + str(YYYY) + '/' + str(MM) + '/' + str(int(DD)), exist_ok=True)

    #Guardar archivo hh_mm_ss.json en la ruta creada
    with open(os.path.join(folder_path + '/' + str(YYYY) + '/' + str(MM) + '/' + str(int(DD)), file_name_js), 'w') as file:
        json.dump(data_js, file)

    #Indica que servicio se va a utilizar
    s3 = boto3.resource('s3')
    #Crear la ruta '/YYYY/MM/DD' en el bucket de S3
    folder_path_s3 = str(YYYY) + '/' + str(MM) + '/' + str(int(DD)) + '/' + file_name_js
    #Se sube el archivo .json al servicio S3
    with open(folder_path_s3, 'rb') as data:
        s3.Bucket(constants.BUCKET_NAME).put_object(Key=folder_path_s3, Body=data)

    print('Done')

upload_folder_s3(None)