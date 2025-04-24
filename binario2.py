#verifico que el numero sea binario (solo tenga 1s y 0s)
def verificar_binario(numero):
    resultado = True
    for digit in range(len(numero)):
      if int(numero[digit]) > 1:
        resultado = False
    return resultado

def numero_a_decimal(numero):
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

#PROGRAMA PRINCIPAL
print(" Conversor y Operaciones Binarias ")
print("1. Convertir Decimal a Binario")
print("2. Convertir Binario a Decimal")
#print("3. Sumar dos números binarios")
#print("4. Restar dos números binarios")
print("3. Salir")

opcion = input("Seleccione una opción: ")

if opcion =="1":
    decimal = int(input("Ingrese el numero decimal: "))
    
    while decimal < 0:
        print("ERROR, el número debe ser positivo")
        decimal = int(input("Ingrese un número entero positivo: "))
    print(f"El número {decimal} en binario es: {decimal_a_binario(decimal)}")
elif opcion=="2":
    binario = input ("Ingrese un numero binario: ")
    while verificar_binario(binario) == False:
        print("ERROR el número ingresado no es válido")
        numero = input("Ingrese un numero binario que desee convertir: ")
    print(f"El número binario {binario} en decimal es {numero_a_decimal(binario)}")
elif opcion=="3":
    print("Chau")
else:
    print("Opcion incorrecta,seleccione una opcion del menu")