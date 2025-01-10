import requests
# URL base del backend
URL_BASE = "https://apielektadev.fos.com.bo/api"

# Credenciales de prueba
CREDENCIALES_VALIDAS = {"email": "admin@fos.com.bo", "password": "12345678"}
DOMINIO_INCORRECTO = {"email": "admin@fost.com.bo", "password": "12345678"}
CREDENCIALES_INVALIDAS = {"email": "user@fos.com.bo", "password": "admins"}