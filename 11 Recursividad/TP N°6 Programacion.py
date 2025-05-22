#Act 1: Crea una función recursiva que calcule el factorial de un número. 
#Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


numero = int(input("Ingresa un número entero mayor que 0: "))


if numero < 1:
    print("Por favor, ingresa un número mayor que 0.")
else:
    print(f"Factoriales del 1 al {numero}:")
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial(i)}")


#Act 2: Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
#Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


posicion = int(input("Ingresa la posición hasta la que deseas ver la serie de Fibonacci (mayor o igual a 0): "))

if posicion < 0:
    print("Por favor, ingresa un número entero mayor o igual a 0.")
else:
    print(f"Serie de Fibonacci hasta la posición {posicion}:")
    for i in range(posicion + 1):
        print(f"F({i}) = {fibonacci(i)}")


#Act 3:Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛**𝑚 = 𝑛 ∗ 𝑛**(𝑚−1).
#Prueba esta función en unalgoritmo general.


def potencia(base, exponente):
    if exponente == 0:
        return 1  
    else:
        return base * potencia(base, exponente - 1)


base = float(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente (entero >= 0): "))

if exponente < 0:
    print("El exponente debe ser un número entero no negativo.")
else:
    resultado = potencia(base, exponente)
    print(f"{base} elevado a la {exponente} es: {resultado}")

#Act 4:Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
#y devuelva su representación en binario como una cadena de texto.


def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("Por favor, ingresa un número entero positivo.")
elif numero == 0:
    print("El número 0 en binario es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")

#Act 5: Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
#y devuelva True si es un palíndromo o False si no lo es. 
#Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True

    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


texto = input("Ingresa una palabra sin espacios ni tildes: ").lower()

if es_palindromo(texto):
    print(f"'{texto}' es un palíndromo.")
else:
    print(f"'{texto}' no es un palíndromo.")



#Act 6: Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.

def suma_digitos(n):
    if n < 10:
        return n 
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("Por favor, ingresa un número positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")


#Act 7: Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), 
#y así sucesivamente hasta llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n)
#que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(n):
    if n == 1:
        return 1  
    else:
        return n + contar_bloques(n - 1)


nivel_inferior = int(input("Ingresa el número de bloques en el nivel más bajo: "))

if nivel_inferior < 1:
    print("Debe ser un número entero positivo mayor o igual a 1.")
else:
    total = contar_bloques(nivel_inferior)
    print(f"Total de bloques necesarios: {total}")


#Act 8: Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), 
#y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        contador = 1 if ultimo == digito else 0
        return contador + contar_digito(numero // 10, digito)


numero = int(input("Ingresa un número entero positivo: "))
digito = int(input("Ingresa el dígito a contar (0-9): "))

if numero < 0 or digito < 0 or digito > 9:
    print("Entrada inválida. Asegúrate de ingresar un número positivo y un dígito entre 0 y 9.")
else:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} vez/veces en el número {numero}.")
