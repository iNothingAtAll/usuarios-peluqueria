# Imagen base
FROM python:3.14.0-alpine3.22


# Establece el directorio de trabajo
WORKDIR /app


# Copia los archivos del proyecto al contenedor
COPY . .


# Dependencias la instalacion de los requerimientos 
RUN apk add build-base


# Instala las dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Expone el puerto por defecto de Flask
EXPOSE 5000


# Variables de entorno para Flask
ENV FLASK_APP=run.py
ENV FLASK_ENV=development


# Comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
