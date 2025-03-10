from fastapi import FastAPI
import google.generativeai as genai
import os

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la Calculadora de Tiempo de Entrega"}

# Configurar API Key de Google directamente en el código (⚠️ No recomendado para producción)
GENAI_API_KEY = "AIzaSyCJIaffMFPeKJaW6VDI0Ols0zrkx9S7rEs"

genai.configure(api_key=GENAI_API_KEY)

# Obtener el puerto desde Railway
PORT = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)