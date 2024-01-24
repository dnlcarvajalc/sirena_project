# **Sirena_project**
>Software with the aim to learn to craft and consume APIs, use AWS services and web skills.

## __Instrucciones de consumo de API__
Para trabajar todos en un mismo entorno y no tener problemas con las diferentes versiones crearemos en conda un entorno virtual para poder manejar la misma versión de python.
1. Para crear el entorno virtual abrimos la terminal de conda y ejecutamos los siguientes comando:
    >- `conda create -n sirena_project python=3.10` (manejaremos la version 3.10 de python)
    >- `conda activate sirena_project` (Para activar el entorno)
>
2. Instalado y activado lo anterior procedemos a instalar una extensión en Visual llamada "Python Environmente Manager" esto con el fin de detectar el entorno que acabamos de crear.
>
3. Para instalar las librerias requeridas por la API debemos correr el archivo de "requirements.txt" de la siguiente manera:
    >- `pip install -r requirements.txt`
>
>***Nota:*** *Para saber todas las dependendias/librerias que tiene nuestro entorno y API existe una herramienta la cual nos permite generar de manera automatica en un archivo tipo texto (requerimients.txt en este ejemplo particular) con dichas dependencias:*
>-`pip freeze > requirements.txt` *(Esto con fines informativos)*
>
4. Dependiendo de la API escogida se instalan las respectivas librerias y con el siguiente comando se ejecuta el programa:
    >- `uvicorn sirena_project:app --reload` (Para la API de FastAPI)
>
5. Por último ir al navegador y buscar [http://localhost:8000]()

