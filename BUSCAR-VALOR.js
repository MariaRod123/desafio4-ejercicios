const array_numeros=[3, 2, 6, 8, 7, 6, 6, 1, 4]

let numero_ingresado = parseInt(prompt("ingrese un numero:"))


function buscarValor(lista, valor){
   let numero_encontrado=lista.indexOf(valor) /* utilizando el método de los array indexOf() busco el número ingresado por su índice dentro del array, si hay varios valores iguales muestra el indice del primero encontrado */
   if (numero_encontrado !==-1){
        return numero_encontrado
    }
    else{
        return -1
    }

}

let lugar_array = buscarValor(array_numeros, numero_ingresado)

if (lugar_array !=-1){
    
    console.log("Valor ingresado:", numero_ingresado, "Posición:", lugar_array)   
}
else{
    console.log("El número ingresado no se encuentra en el array")
}

