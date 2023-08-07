
numero_ingresado = int(input("Ingrese un valor: "))

lista_numeros = [3, 2, 6, 8, 7, 6, 6, 1,4]


def buscar_valor(lista, valor):
    if valor in lista:
        numero_encontrado=lista.index(valor) #index(): método que busca un elemento por su indice  dentro de una lista
        return numero_encontrado
    else:
        return -1

lugar_lista = buscar_valor(lista_numeros, numero_ingresado)

if lugar_lista != -1:
    print ("Valor ingresado:", numero_ingresado, " posición:", lugar_lista)
else:
    print ("El número ingresado no se encuentra en la lista.")


