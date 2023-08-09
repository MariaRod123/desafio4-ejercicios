import requests

pais_ingresado = input("Ingrese el nombre de un pais:")

paises_sudamerica = {'Argentina': ['Buenos Aires', 'Bariloche', 'Mendoza', 'Concordia', 'Ushuaia', 'Mar del Plata'],
                     'Bolivia': ['La Paz', 'Sucre', 'Cochabamba','Santa Cruz de la Sierra '],
                     'Brasil': ['Brasilia', 'Sao Paulo', 'Rio de Janeiro', 'Recife', 'Natal', 'Fortaleza', 'Curitiba'],
                     'Chile': ['Santiago', 'Valparaiso', 'Viña del Mar'],
                     'Colombia': ['Bogotá', 'Medellin', 'Cartagena', 'Cali'], 'Ecuador': ['Quito', 'Guayaquil'],
                     'Panama': ['Ciudad de Panamá', 'Bajo Boquete'],
                     'Paraguay': ['Asunción', 'Ciudad del Este', 'Concepción', 'Luque'], 'Perú': ['Lima',' Arequipa','Cusco', 'Trujillo', 'Iquitos'],
                     'Uruguay': ['Montevideo', 'Salto', 'Paysandu', 'Rocha', 'Durazno', 'Minas', 'Melo', 'Rivera', 'Artigas', 'Maldonado', 'Treinta y Tres', 'Canelones', 'San José de Mayo', 'Mercedes', 'Colonia del Sacramento', 'Trinidad', 'Florida', 'Fray Bentos', 'Tacuarembó'],
                     'Venezuela': ['Caracas', 'Maracaibo', 'Valencia', 'Barquisimeto']}



def mostrar_ciudades_del_pais(pais):
    if pais in paises_sudamerica:
        ciudades = paises_sudamerica[pais]
        print("Ciudades disponibles en: ", pais)
        for ciudad in ciudades:
            print(ciudad)
        return ciudades
    else:
        print("Pais no encontrado")
        return []

def obtener_datos_tiempo(ciudad):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=896ead403d5e70c132fe1886fe5ab88f&units=metric&lang=es".format(
        ciudad)

    respuesta = requests.get(url)
    datos_tiempo = respuesta.json()
    ciudad = datos_tiempo['name']
    pais = datos_tiempo['sys']['country']
    temperatura = datos_tiempo['main']['temp']
    maxima = datos_tiempo['main']['temp_max']
    minima = datos_tiempo['main']['temp_min']
    estado_tiempo = datos_tiempo['weather'][0]['description']

    return {'Pais': pais, 'Ciudad': ciudad, 'Temperatura en °C': round(temperatura, 1),
            'Máxima en °C': round(maxima, 1), 'Mínima en °C': round(minima, 1), 'Estado actual': estado_tiempo}



ciudades_disponibles = mostrar_ciudades_del_pais(pais_ingresado)
if ciudades_disponibles:
    for ciudad in ciudades_disponibles:
        tiempo=obtener_datos_tiempo(ciudad)
        print("Condiciones del tiempo actuales:",tiempo)


