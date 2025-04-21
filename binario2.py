#verifico que el numero sea binario (solo tenga 1s y 0s)
def verificar_binario(numero):
    resultado = True
    for digit in range(len(numero)):
      if int(numero[digit]) > 1:
        resultado = False
    return resultado

def numero_a_decimal():
    numero = input("Ingrese un número binario para convertir a decimal: ")
    if verificar_binario(numero) == True:
        suma = 0
        for i in range(len(numero)):
            numero = int(numero)
            digito = numero % 10
            numero = numero // 10
            suma += (2 ** i) * digito
        print(f"El número binario {numero} en decimal es {suma}")  #esto despues podriamos sacarlo y ponerlo en el menu principal del conversor?
        #pienso que no siempre vamos a querer que esta funcion imprima algo. Por ejemplo cuando la reutilicemos para la suma de binarios. No vamos a querer que diga "este numero es tan en decimal",
        #sino que sume y listo, no?
        return suma
    else:
      print("El número ingresado no es un número binario válido")
    
print(numero_a_decimal())