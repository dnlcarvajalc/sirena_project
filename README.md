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


# **Configuración de credenciales con AWS CLI**
Para poder acceder al servicio S3 de AWS desde python debemos instalar la interfaz de línea de comandos de AWS. Siguiendo los siguientes pasos.
>
1. Instalación de ***AWS CLI***.
    >- Primero debemos ingresar a la página de **AWS** y descargar el instalador para el sistema operativo que estemos utilizando.
    [https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html]()
    >-  Ejecutamos el instalador.
    >- Y verificamos que se haya instalado correctamente, abrimos una ventana del símbolo del sistema y ejecutamos el siguiente comando `aws --version`; y nos debe aparecer lo siguiente:
    **aws-cli/2.10.0 Python/3.11.2 Windows/10 exe/AMD64 prompt/off**
>
2. Una vez instalado el ***AWS CLI*** procedemos realizar la configuración de las credenciales:
    >- Abrimos una ventana del símbolo del sistema (**cmd**) ejecutamos el siguiente comando:
    `aws configure`
    >- Especificamos las claves de acceso y damos *ENTER*.
    >- Ahora ingresamos una región predeterminada: ***us-east-1***
    >- Damos *ENTER* y así terminamos nuestra configuración de credenciales. Para ver los pasos más detallados podemos consultar la siguiente página. [https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration]()
>
3. Ya con las instalaciones realizadas y la configuración de credenciales hecha no deberíamos tener inconvenientes al ejecutar nuestro proyecto.

# **FRONTEND: Documentación del proyecto**
El proyecto "Sirena_project" tiene como objetivo proporcionar a los usuarios una experiencia única de exploración global.
En la interfaz frontend, los usuarios pueden descubrir imágenes aleatorias de distintos lugares turísticos o paisajes, con su respectiva descripción. La interfaz es sencilla e intuitiva, invitando a los usuarios a explorar y aprender sobre diferentes lugares del mundo.

`python src/SIRENA_PROJECT.py`
>
1. ***Estado del proyecto***
    El proyecto se encuentra actualmente en desarrollo, y aún falta integrar la parte del FRONTEND con el BACKEND. Se están realizando esfuerzos para mejorar la funcionalidad y la experiencia del usuario.
>
2. ***Utilidad del proyecto***
    >- **Exploración Global:** Permite a los usuarios descubrir y aprender sobre diferentes lugares del mundo de manera aleatoria.
    >- **Experiencia Única:** Ofrece una experiencia visual atractiva con imágenes y descripciones de lugares turísticos.
    >- **Fácil de Usar:** La interfaz sencilla y amigable invita a los usuarios a explorar sin complicaciones.
>
3. ***Estructura del FRONTEND***
    El frontend del proyecto está compuesto por archivos HTML, CSS y JavaScript.
    A continuación, se presenta una breve descripción de cada archivo:
    >- **HTML (index.html):** Define la estructura principal de la página web, incluyendo elementos como el contenedor de imágenes, botones y efectos visuales.
    >- **CSS (app.css):** Contiene estilos y diseño para la apariencia visual del proyecto, asegurando una presentación atractiva y responsive en diferentes dispositivos.
    >- **JavaScript (main.js):** Gestiona la lógica de la aplicación, como la carga de imágenes aleatorias y la presentación de información relacionada.
>
4. ***Dependencias***
    El frontend del proyecto hace uso de diversas bibliotecas y herramientas que contribuyen a su funcionalidad y presentación. A continuación, se presentan las dependencias clave utilizadas en este proyecto.
    >- **Axios:** Es una biblioteca utilizada para realizar peticiones HTTP, en este caso, para obtener imágenes aleatorias de la API de Unsplash. Se incluye mediante el siguiente script:
    `<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>`
    >- **Google Fonts:** La fuente "Mulish" de Google Fonts se importa en el archivo CSS para dar estilo al texto en la página, para así asegurar una presentación agradable y legible. Se incluye en la sección de estilos del archivo CSS.
    `@import url('https://fonts.googleapis.com/css2?family=Mulish:wght@200;700&display=swap');`
>
5. ***Instrucciones de Uso***
    >- **1:** Clona el repositorio en tu máquina local.
    >- **2:** Abre el archivo `index.html` en tu navegador web.
    >- **3:** Explora diferentes lugares haciendo clic en el botón "Conocer Lugar".

    ![Previsualización página web](./frontend/img/web.png)
>
6. ***Contribuciones***
    El proyecto es mantenido y desarrollado por un equipo de ingenieros electrónicos:
    - Daniela Villamizar
    - Manuela Correa
    - Lina Franco
    - Jacobo Montenegro
    - Juan Sebastián Cortes
    - Daniel Carvajal
    - Juan José Gómez
>
Cualquier contribución o sugerencia para mejorar el proyecto es altamente apreciada.
