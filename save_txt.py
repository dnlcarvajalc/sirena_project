import os
import json

#Crear archivo hh_mm_ss.json
file_name_js = 'hh_mm_ss.json'
data_js = {'hh': ' ', 'mm': ' ', 'ss': ' '}

#Obtener ruta de la carpeta actual
folder_path = os.path.abspath(os.getcwd())
#Crear la ruta '/YYYY/MM/DD' en la carpeta actual
os.makedirs(folder_path + '/YYYY/MM/DD', exist_ok=True)

#Guardar archivo hh_mm_ss.json en la ruta creada
with open(os.path.join(folder_path + '/YYYY/MM/DD', file_name_js), 'w') as file:
    json.dump(data_js, file)


