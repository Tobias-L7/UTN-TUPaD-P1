#Actividades 
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100                 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.


num1 = -1
for i in range(num1, 100, 1):
    num1 += 1
    print(f"{num1}")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.


num = int(input("Ingrese un numero entero: "))
digitos = len(str(abs(num)))
print(f"tiene digitos {digitos} el numero {num}")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

numero = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

suma = 0

if numero > num2:
    numero, num2 = num2, numero

for i in range(numero + 1, num2):
    suma += i

print("La suma de los números entre", numero, "y", num2, "es:", suma)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

num_usu = int(input("Ingresa un numero entero(0 para detenerse): "))

sumatoria = 0
while num_usu != 0:
    sumatoria += num_usu
    num_usu = int(input("Ingresa un numero entero(0 para detenerse): "))

print("La suma de los números es:", sumatoria)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
nume = int(input("Adivina el numero entre el 0 y 9: "))
numero_aleatorio = random.randint(0, 9)
cont = 0

while numero_aleatorio != nume:
    cont += 1
    print("Numero incorrecto, sigue intentando")
    nume = int(input("Adivina el numero entre el 0 y 9: "))
    
if numero_aleatorio == nume:
    cont += 1

print (f"Felicitaciones, has adivinado el numero, tuviste {cont} intentos para acertar el numero")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for pares in range (100, -1, -1):
    if pares % 2 == 0:
        print (f"{pares}")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

final_usuario = int(input("Ingrese un numero entero positivo: "))
inicio = 0
suma = 0

while final_usuario < inicio:
    if final_usuario < inicio:
        final_usuario = int(input("el numero debe ser positivo, elige otro numero: "))

for i in range(inicio + 1, final_usuario):
    suma += i

print(F"la suma total entre los numeros 0 y {final_usuario} es {suma}")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
positivos = 0
negativos = 0
cantidad = 100

for i in range (1, cantidad + 1):
    num = int(input(f"{i}) Ingrese un numero entero: "))
    if num % 2 == 0:
        pares += 1
    if num < 0:
        negativos += 1
    if num % 2 != 0:
        impares += 1
    if num > 0:
        positivos += 1

print(f"numeros positivos = {positivos}")
print(f"numeros negativos = {negativos}")
print(f"numeros pares = {pares}")
print(f"numeros impares = {impares}")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

cantidad = 100
suma = 0

for i in range (1, cantidad + 1):
    num = int(input(f"{i}) Ingrese un numero entero: "))
    suma += num

media = suma / cantidad
print(f"la suma de sus valores son {suma} y la media es de {media}")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

num_usu = int(input("Ingrese un numero: "))

invertido = 0
num = abs(num_usu) 

while num != 0:
    digito = num % 10          
    invertido = invertido * 10 + digito  
    num //= 10                  

if num_usu < 0:
    invertido = -invertido

print("Número invertido:", invertido)



