
#verifico que el numero sea binario (solo tenga 1s y 0s)
def verificar_binario(numero):
    resultado = True
    for digit in range(len(numero)):
      if int(numero[digit]) > 1:
        resultado = False
    return resultado

def binario_a_decimal(numero):
        suma = 0
        for i in range(len(numero)):
            numero = int(numero)
            digito = numero % 10
            numero = numero // 10
            suma += (2 ** i) * digito
        return suma
    
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
    return numero_final

def ingrese_binario():
    binario = input("Ingrese un numero binario: ")
    while verificar_binario(binario) == False:
        print("ERROR el número ingresado no es válido")
        binario = input("Ingrese un numero binario: ")
    binario = binario_a_decimal(binario)
    return binario

def ingrese_decimal():
    decimal = int(input("Ingrese un numero entero positivo: "))
    while decimal < 0:
        print("ERROR, el número debe ser positivo")
        decimal = int(input("Ingrese un número entero positivo: "))
    decimal = decimal_a_binario(decimal)
    return decimal

#PROGRAMA PRINCIPAL
print(" Conversor y Operaciones Binarias ")
print("1. Convertir Decimal a Binario")
print("2. Convertir Binario a Decimal")
print("3. Sumar dos números binarios")
print("4. Restar dos números binarios")
print("5. Salir")

opcion = input("Seleccione una opción: ")

if opcion =="1":
    decimal = ingrese_decimal()
    print(f"El número {binario_a_decimal(decimal)} en binario es: {decimal}")
elif opcion=="2":
    binario = ingrese_binario()
    print(f"El número binario {decimal_a_binario(binario)} en decimal es {binario}")
elif opcion =="3":
    binario1 = ingrese_binario()
    binario2 = ingrese_binario()
    suma = binario1 + binario2
    print(f"La suma entre {decimal_a_binario(binario1)} y {decimal_a_binario(binario2)} es {decimal_a_binario(suma)}")  
elif opcion == "4":
    binario1 = ingrese_binario()
    binario2 = ingrese_binario()
    if binario1 > binario2:
        resta = binario1 - binario2
        print(f"La resta entre {decimal_a_binario(binario1)} y {decimal_a_binario(binario2)} es {decimal_a_binario(resta)}")      
    else:
        print("ERROR, esta calculadora no soporta resultados negativos. Esté atento a una próxima versión mejorada.")
elif opcion=="5":
    print("Chau")
else:
    print("Opción incorrecta, seleccione una opcion del menú")