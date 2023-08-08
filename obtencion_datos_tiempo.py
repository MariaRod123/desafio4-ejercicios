import requests
import csv


def obtener_datos_tiempo(ciudad):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=896ead403d5e70c132fe1886fe5ab88f&units=metric&lang=es".format(
        ciudad)
    respuesta = requests.get(url)
    datos_tiempo = respuesta.json()
    pais = datos_tiempo['sys']['country']
    sensacion_termica = datos_tiempo['main']['feels_like']
    maxima = datos_tiempo['main']['temp_max']
    minima = datos_tiempo['main']['temp_min']
    presion_atmosferica = datos_tiempo['main']['pressure']
    humedad = datos_tiempo['main']['humidity']

    estado_tiempo = datos_tiempo['weather'][0]['description']

    return [ciudad, pais, round(sensacion_termica,1), round(maxima,1), round(minima,1), presion_atmosferica, humedad, estado_tiempo]


paises_latam = {'Argentina': 'Buenos Aires', 'Bolivia': 'La Paz', 'Brasil': 'Brasilia', 'Chile': 'Santiago',
                'Colombia': 'Bogotá', 'Costa Rica': 'San José', 'Cuba': 'La Habana', 'Ecuador': 'Quito',
                'El Salvador': 'San Salvador', 'Guatemala': 'Ciudad de Guatemala', 'Honduras': 'Tegucigalpa',
                'México': 'Ciudad de Mexico', 'Nicaragua': 'Managua', 'Panamá': 'Ciudad de Panamá',
                'Paraguay': 'Asunción', 'Perú': 'Lima', 'República Dominicana': 'Santo Domingo',
                'Uruguay': 'Montevideo', 'Venezuela': 'Caracas'}


# Nombre del archivo CSV
archivo_csv = "datos_tiempo.csv"

# Abre el archivo CSV en modo de escritura
documento = open(archivo_csv, mode="w", newline="", encoding="utf-8")
writer = csv.writer(documento, delimiter=";")

# escribe los nombres de las columnas en el archivo CSV
writer.writerow(
    ["Ciudad", "Pais", "Sensacion termica (°C) ", "Temperatura Maxima (°C)", "Temperatura Minima (°C)", "Presion (hPa)",
     "Humedad(%)", "Estado Actual"])

# muestra en pantalla los datos que obtiene de la api y va escribiendo los datos de cada pais en una fila del archivo
for pais, capital in paises_latam.items():
    estado_tiempo_por_pais = obtener_datos_tiempo(capital)
    print("Condiciones del tiempo actuales:", estado_tiempo_por_pais)
    writer.writerow(estado_tiempo_por_pais)
    print("Guardando datos, aguarde un momento...")

# Cierra el archivo
documento.close()

print("Datos guardados en el directorio actual en el archivo CSV:", archivo_csv)
