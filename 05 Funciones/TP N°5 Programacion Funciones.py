#Act 1: Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: 
# “Hola Mundo!”. Llamar a esta función desde elprograma principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

#Programa Principal 
imprimir_hola_mundo()


#Act 2:Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}! Bienvenido!")

#Programa Principal
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)


#Act 3: Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
#“Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Programa Principal
a = input("ingrese su nombre: ")
b = input("Ingrese su apellido: ")
c = input("Ingrese su edad: ")
d = input("Ingrese su residencia: ")
informacion_personal(a, b, c, d)


#Act 4: Crear dos funciones: 
#calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
#calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.


def calcular_area_circulo(radio):
    return 3.1416 * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * 3.1416 * radio

#Programa Principal
radio = float(input("Ingrese el radio del circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es {area}")
print(f"El area del circulo es {perimetro}")


#Act 5: Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
#Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos // 3600

#Programa Principal
segundos = int(input("Ingrese los segundos para pasarlos a horas: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivale a {horas} horas")



#Act 6: Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. 
#Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(0, 11):
        resultado = numero * i
        print(f"{numero}x{i}={resultado}")

#Programa principal
numero = int(input("Ingrese un numero: "))
tabla = tabla_multiplicar(numero)



#Act 7: Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
#Mostrar los resultados de forma clara.

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        print("no se puede dividir por cero")
    return(suma, resta, multiplicacion, division)

#Programa Principal
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

resultados = operaciones_basicas(a, b)

print(f"\nTupla devuelta: {resultados}")

print("\nResultados detallados:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")



#Act 8: Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). 
#Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.


def calcular_imc(peso, altura):
    if altura <= 0:
        return "Altura inválida. Debe ser mayor que cero."
    return peso / (altura ** 2)

#Programa Principal
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Su indice de masa corporal es de {imc}")


#Act 9: Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. 
#Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return print(f"la temperatura en Fahrenheit es de {fahrenheit}°F")

#Programa Principal
celsius = float(input("Ingrese la temperatura en Celsius: "))
celsius_a_fahrenheit(celsius)



#Act 10: Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    suma = a + b + c
    promedio = suma / 3
    return promedio


#Programa Principal
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de estos tres numeros es de {promedio}")




