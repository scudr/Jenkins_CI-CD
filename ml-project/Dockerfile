# Utiliza la imagen oficial de Python 3.9 de Docker Hub como imagen base
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor en /app.
# Todos los comandos subsiguientes se ejecutarán desde este directorio.
WORKDIR /app

# Copia el contenido del directorio actual (donde se encuentra el Dockerfile)
# dentro del contenedor en /app. Esto incluye todos los archivos y subdirectorios.
COPY . .

# Ejecuta el comando para instalar las dependencias de Python definidas en requirements.txt.
# Esto se hace dentro del sistema de archivos del contenedor.
RUN pip install -r requirements.txt

# Establece el comando predeterminado para ejecutar el contenedor. Este comando inicia un servidor Uvicorn
# que aloja una aplicación FastAPI definida en el módulo app (app.py) y escucha en todas las
# interfaces de red (0.0.0.0) en el puerto 8000. Esta configuración es típica para que una aplicación web
# sea accesible desde fuera del contenedor.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]