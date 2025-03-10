from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import google.generativeai as genai

# Configurar FastAPI
app = FastAPI()

# Configurar Jinja2 para servir plantillas HTML
templates = Jinja2Templates(directory="templates")

# 🔹 API Key de Google directamente en el código (⚠️ NO RECOMENDADO para producción)
GENAI_API_KEY = "AIzaSyCJIaffMFPeKJaW6VDI0Ols0zrkx9S7rEs"  # Reemplaza con tu clave real

# Configurar la API Key
genai.configure(api_key=GENAI_API_KEY)

# Ruta para servir la página principal
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Ruta para calcular el tiempo de entrega
@app.get("/calcular/")
def calcular_tiempo(distancia_km: float):
    tiempo_viaje = (distancia_km / 2) * 60  # Convertir horas a minutos
    tiempo_total = tiempo_viaje + 10  # Sumar 10 minutos de preparación

    # Usar un modelo que tienes disponible
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(
        f"Si la comida tarda 10 minutos en prepararse y el robot viaja a 2 km/h, ¿en cuánto tiempo llega si está a {distancia_km} km? Responde de forma clara y amigable."
    )

    return {
        "tiempo_estimado_minutos": round(tiempo_total, 2),
        "respuesta_ai": response.text
    }
