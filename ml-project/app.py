# Importamos las bibliotecas necesarias
import uvicorn 
from fastapi import FastAPI, File, UploadFile, Depends
import pandas as pd
from pydantic import BaseModel
import tempfile  # Biblioteca para crear archivos temporales
import shutil  # Biblioteca para copiar archivos
import joblib

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir un endpoint para la raíz con método GET
@app.get("/")
def home():
    # Retorna un simple mensaje de texto
    return 'Hola mundo: Model API - VERSION 1'

# Definir un endpoint para manejar la subida de archivos Excel
@app.post("/upload-excel")
def upload_excel(file: UploadFile = File(...)):
    try:
        # Crear un archivo temporal para manejar el archivo subido
        with tempfile.TemporaryFile() as temp_file:
            # Copiar el contenido del archivo subido al archivo temporal
            shutil.copyfileobj(file.file, temp_file)

            # Volver al principio del archivo temporal
            temp_file.seek(0)

            # Leer el archivo Excel usando pandas y almacenarlo en un DataFrame
            df = pd.read_excel(temp_file)

            ##### MODIFICACIONES V2 #########

            # Cargar el modelo
            loaded_model = joblib.load('train/iris_model.joblib')

            # Realizar predicciones con el modelo cargado
            new_predictions = loaded_model.predict(df.values)

            # Retornar las predicciones
            return {"predictions": new_predictions.tolist()}
    except Exception as e:
        # Retornar un mensaje de error si ocurre alguna excepción
        return {"error": f"Ocurrió un error: {str(e)}"}
