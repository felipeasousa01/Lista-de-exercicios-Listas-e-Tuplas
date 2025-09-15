# Instale a biblioteca requests e faça uma requisição para o site https://www.google.com.
import requests
response = requests.get("https://www.google.com")
if response.status_code == 200:
    print("Requisição bem-sucedida!")