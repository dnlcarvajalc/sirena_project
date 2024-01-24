from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

#directory = ubicación de la carpeta donde se ubican el html
templates = Jinja2Templates(directory="templates") 

#Respuesta de la petición (Corresponde a la dirección donde estan los templates y ubicacion de la pagina)
@app.get("/")
def read_root(request: Request):

    return templates.TemplateResponse("main_template.html", {"request": request})