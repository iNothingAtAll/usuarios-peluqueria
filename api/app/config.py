from os.path import abspath, dirname, join
from os import getenv
from dotenv import load_dotenv


# Leer el archivo .env para configurar la api
basedir = abspath(dirname(__file__))
load_dotenv(join(basedir, '..', '.mariadb.env'))


# Se extraen las variables de entorno en .env
class Config:


    # Informacion acerca de la conexion local
    MYSQL_HOST = getenv("MYSQL_HOST", "mariadb")
    MYSQL_PORT = getenv("MYSQL_PORT", "3306")


    # Informacion de login para la base de datos
    MYSQL_USER = getenv("MYSQL_USER")
    MYSQL_PASSWORD = getenv("MYSQL_PASSWORD")
    MYSQL_DATABASE = getenv("MYSQL_DATABASE")


    # Clave de acceso para restringir las peticiones
    API_KEY_ACCESS = getenv("API_KEY_ACCESS", "1234")


    # Variables para que SQLAlchemy se conecte a la base de datos
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False