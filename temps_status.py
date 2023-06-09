# Busca les condicions meteorològiques d'un lloc en concret

import requests
import json

def get_status(poble):
    try:
        response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key=8e3a9372e503477ca0f210354231404&q={poble}&days=1&aqi=no&alerts=no")

        poblacio = response.json()["location"]["name"]
        pais = response.json()["location"]["country"]
        temperatura = response.json()["current"]["temp_c"]
        humitat = response.json()["current"]["humidity"]
        presio = response.json()["current"]["pressure_mb"]
        data= response.json()["current"]["last_updated"]
        pluja = response.json()["current"]["precip_mm"]
        condicions = response.json()["current"]["condition"]["text"]

        return poblacio, pais, temperatura, humitat, presio, data, pluja, condicions
    except Exception as e:
        print(f"Hi ha hagut un error amb la funció get_status >>>>> {e}")