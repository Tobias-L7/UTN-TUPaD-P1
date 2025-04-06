#Trabajo Practico N°3: Estructuras Condicionales

#Acitvidad 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("ingrese su edad: "))
mayor_edad = 18

if edad >= mayor_edad:
    print("Es mayor de edad")
else:
    print("No eres mayor de edad")

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Acitvidad 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = float(input("Ingrese su nota: "))
aprobado = 6

if nota >= aprobado:
    print("Estas Aprobado")
else:
    print("Estas Desaprobado")

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Acitvidad 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
#en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
#Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

par = int(input("Ingrese un numero par: "))

if par % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Porfavor, ingrese un numero par")

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Acitvidad 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de lassiguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Eres un Niño/a")
elif edad >= 12 and edad < 18:
    print("Eres un Adolescente")
elif edad >= 18 and edad < 30:
    print("Eres un Adulto/a joven")
elif edad >= 30:
    print("Eres un Adulto/a")
else:
    pass

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Acitvidad 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres(incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir en pantalla el mensaje "Ha ingresado una contraseña correcta";
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contraseña = input("ingrese una contraseña de entre 8 y 14 caracteres: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Porfavor, ingrese una contraseña de entre 8 y 14 caracteres")

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Acitvidad 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. 
# Imprimir el resultado por pantalla

import random
from statistics import mode, median, mean   

numeros_aleatorios = [random.randint(1, 10) for i in range(10)]

print("Números aleatorios:", numeros_aleatorios)

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(f"media:{media}")
print(f"mediana:{mediana}")
print(f"moda:{moda}")

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("No hay sesgo")
else:
    pass

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Actividad 7) Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("ingrese una palabra o frase: ")

vocal = "a" "e" "i" "o" "u"
if frase[-1].lower() in vocal:
    frase += "!"

print(f"resultado: {frase}")

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Actividad 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")
print("Elige 1. Si quiere su nombre en mayúsculas")
print("Elige 2. Si quiere su nombre en minúsculas")
print("Elige 3. Si quiere su nombre con la primera letra mayúscula")

tipo = int(input("Elige el numero segun las opciones: "))

if tipo == 1:
    nombre = nombre.upper()
    print(f"Su nombre quedo asi:",nombre)
elif tipo == 2:
    nombre = nombre.lower()
    print(f"Su nombre quedo asi:",nombre)
elif tipo == 3:
    nombre = nombre.title()
    print(f"Su nombre quedo asi:",nombre)
else:
    print("Porfavor, elige una opcion")

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Actividad 9) Escribir un programa que pida al usuario la magnitud de un terremoto, 
#clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" 
#● Mayor o igual que 3 y menor que 4: "Leve" 
#● Mayor o igual que 4 y menor que 5: "Moderado" 
#● Mayor o igual que 5 y menor que 6: "Fuerte" 
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" 
#● Mayor o igual que 7: "Extremo" 

magnitud = float(input("ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte")
elif magnitud >= 7:
    print("Extremo")
else:
    pass

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Actividad 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

def obtener_estacion(mes, dia, hemisferio):
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    else:
        return "Fecha inválida"

    return estacion_norte if hemisferio == "N" else estacion_sur

estacion = obtener_estacion(mes, dia, hemisferio)
print("Estás en:", estacion)