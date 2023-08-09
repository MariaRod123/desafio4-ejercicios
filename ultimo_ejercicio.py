import requests

pais_ingresado = input("Ingrese el nombre de un pais:")


def obtener_datos_tiempo(pais):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=896ead403d5e70c132fe1886fe5ab88f&units=metric&lang=es".format(
        pais)
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos_tiempo = respuesta.json()
        pais = datos_tiempo['sys']['country']
        temperatura = datos_tiempo['main']['temp']
        maxima = datos_tiempo['main']['temp_max']
        minima = datos_tiempo['main']['temp_min']
        estado_tiempo = datos_tiempo['weather'][0]['description']

        return {'Pais': pais, 'Temperatura en °C': round(temperatura, 1),
                'Máxima en °C': round(maxima, 1), 'Mínima en °C': round(minima, 1), 'Estado actual': estado_tiempo}
    else:
        print("No se encuentra el pais ingresado:", format(respuesta.status_code))


print(obtener_datos_tiempo(pais_ingresado))
