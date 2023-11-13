# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8080 (ajusta según sea necesario)
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "receive_data.py"]

