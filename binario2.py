#FUNCIONES

#Verifico que el numero sea binario (solo tenga 1s y 0s)
def verificar_binario(numero):
    resultado = True
    for digit in range(len(numero)):
      if int(numero[digit]) > 1:
        resultado = False
    return resultado

#Convierte un número binario a decimal y la retorna.
def binario_a_decimal(numero):
#Definimos la variable suma con valor 0, esta variable será la encargada 
#de almacenar el valor decimal resultante       
        suma = 0
        for i in range(len(numero)):
            numero = int(numero)
            digito = numero % 10 #Se utiliza el operador módulo (%) para obtener el último dígito del número entero numero.
            numero = numero // 10 #Se utiliza la división entera (//) para eliminar el último dígito del número entero numero.
            suma += (2 ** i) * digito
        return suma
   
def decimal_a_binario(numero): #Convierte un número decimal a binario y la retorna como string.
#Definimos las variables a utilizar en la funcion, restos como una lista vacía y numero_final como una cadena vacía
    restos = [] 
    numero_final = "" 
#Comenzamos un bucle while mientras el numero ingresado sea mayor a 0 y en cada iteración 
#se calculará el residuo y lo guardaremos en la lista "restos"    
    while numero > 0: 
        resto = numero % 2 
        numero = numero // 2
        restos.append(resto) 
    restos = reversed(restos) 
#Con un bucle for en cada iteración el valor del residuo i se convierte en una cadena y se concatena al final 
#de la cadena numero_final que es el valor que retorna la función.    
    for i in restos: 
        numero_final += str(i) 
    return numero_final

#La siguiente función sirve para corroborar que el número ingresado sea un número binario y retorne 
# el valor ingresado directamente convertido en su equivalente en decimal.
def ingrese_binario():
    binario = input("Ingrese un numero binario: ")
    while verificar_binario(binario) == False:
        print("ERROR el número ingresado no es válido")
        binario = input("Ingrese un numero binario: ")
#Aquí reutilizamos la función binario_a_decimal para transformar el número binario corroborado en decimal 
#y la función lo retorna.
    binario = binario_a_decimal(binario)
    return binario

#Esta función sirve para corroborar que el número ingresado sea entero positivo y retorne el valor ingresado
#directamente convertido en su equivalente en binario.
def ingrese_decimal():  
    decimal = int(input("Ingrese un numero entero positivo: "))
    while decimal < 0:
        print("ERROR, el número debe ser positivo")
        decimal = int(input("Ingrese un número entero positivo: "))
#Aquí reutilizamos la función decimal_a_binario para transformar el número decimal corroborado en binario 
# y la función lo retorna.
    decimal = decimal_a_binario(decimal) 
    return decimal


#PROGRAMA PRINCIPAL
print(" Conversor y Operaciones Binarias ")
print("1. Convertir Decimal a Binario")
print("2. Convertir Binario a Decimal")
print("3. Sumar dos números binarios")
print("4. Restar dos números binarios")
print("5. Salir")
#A continuación le pedimos por consola que seleccione una de las opciones antes definidas
#del programa principal.
opcion = input("Seleccione una opción: ")
#Con un condicional if seguido de elif (para cada opción) 
#se realiza la operación pertinente.
if opcion =="1":
    decimal = ingrese_decimal()#Llamamos a la función ingrese_decimal() 
    #Mostramos por pantalla el resultado, donde dentro del print llamamos también a la función binario_a_decimal
    #para convertir el número ingresado nuevamente en base 10 para mostrar por pantalla y luego la conversión.
    print(f"El número {binario_a_decimal(decimal)} en binario es: {decimal}")
elif opcion=="2": #Se repiten en las opciones "2", "3" y "4" las operaciones de la opción 1 cambiando las funciones pertinentes.
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
    #En caso de que el numero ingresado para binario1 sea menor a binario2 mostramos por pantalla el siguiente mensaje:
    else:
        print("ERROR, esta calculadora no soporta resultados negativos. Esté atento a una próxima versión mejorada.")
elif opcion=="5":
    print("Chau")
#Si el usuario ingresa un número que no se encuentra en el menú mostramos por consola el siguiente mensaje:
else:
    print("Opción incorrecta, seleccione una opcion del menú")