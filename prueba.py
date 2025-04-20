def decimal_a_binario(numero):
    numero = int(input("Ingrese un numero entero positivo: "))
    if numero >= 0:
        while numero > 0:
            numero = numero / 2
            


#Le pedimos un numero binario por consola al usuario en forma de string así toma como válido todo número
#que comience con 0 (cero).
numero = input("Ingrese un número binario a convertir: ")
suma = 0

#obtengo el indice del digito empezando desde la derecha
for i in range(len(numero)):
    numero = int(numero)
    digito = numero % 10
    numero = numero // 10
    if digito == 1:
        suma += 2 ** i
print(f"El número en decimal es: {suma}")

