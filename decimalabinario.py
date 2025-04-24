def decimal_a_binario(numero):
    restos = [] #Armamos una variable como lista (vacía) para luego utilizarla para agregarle los módulos del número ingresado.
    numero_final = "" #Definimos la variable numero_final como una cadena (aunque por el momento sin ningún valor)
    while numero > 0: #Comenzamos el bucle while, mientras el número ingresado sea mayor a 0.
        resto = numero % 2 #Del número ingresado por el usuario, extraemos el resto, producto de dividirlo por 2.
        numero = numero // 2
        restos.append(resto) #Guardamos el resto en la lista "restos" con la función .append (que sirve para agregar elementos a la lista)
    restos = reversed(restos) #Luego de que el bucle finalice, utilizamos la función reversed para invertir el orden de los elementos en la lista.
    for i in restos: #Realizamos un bucle for para iterar hasta la cantidad de elementos de la lista restos.
        numero_final += str(i) 
    return numero_final #Retornamos el número final.


numero = int(input("Ingrese un numero entero positivo: "))

while numero < 0:
    print("ERROR, el número debe ser positivo")
    numero = int(input("Ingrese un número entero positivo: "))
print(decimal_a_binario(numero))