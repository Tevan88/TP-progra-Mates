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
    

numero = input("Ingrese un numero binario que desee convertir: ")
while verificar_binario(numero) == False:
   print("ERROR el número ingresado no es válido")
   numero = input("Ingrese un numero binario que desee convertir: ")

print(f"El número binario {numero} en decimal es {numero_a_decimal(numero)}")  #esto despues podriamos sacarlo y ponerlo en el menu principal del conversor?
        #pienso que no siempre vamos a querer que esta funcion imprima algo. Por ejemplo cuando la reutilicemos para la suma de binarios. No vamos a querer que diga "este numero es tan en decimal",
        #sino que sume y listo, no?