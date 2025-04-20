def decimal_a_binario(numero):
    restos = []
    numero_final = ""
    while numero > 0:
        resto = numero % 2
        numero = numero // 2
        restos.append(resto) 
    restos = reversed(restos)
    for i in restos:
        numero_final += str(i)
    return numero_final


numero = int(input("Ingrese un numero entero positivo: "))
while numero < 0:
    print("ERROR, el número debe ser positivo")
    numero = int(input("Ingrese un número entero positivo: "))
print(decimal_a_binario(numero))