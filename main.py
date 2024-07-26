# Función de Saludo

def saludar(nombre):
    return f"Hola, {nombre}! ¿Cómo estás hoy?"

nombre = input("Cuál es tu nombre?: ")
print(saludar(nombre))

# Número Par o Impar

def es_par(numero):

    return numero % 2 == 0

def es_impar(numero):

    return numero % 2 != 0

def main():
    numero = int(input("Introduce un número entero: "))
    
    if es_par(numero):
        print(f"El número {numero} es par.")
    elif es_impar(numero):
        print(f"El número {numero} es impar.")
    else:
        print("Ha ocurrido un error.")

if __name__ == "__main__":
    main()

# Función de Suma

def sumar(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Ambos argumentos deben ser números enteros."

    return a + b

num1 = input("Digita el primer número: ")
num2 = input("Digita el segundo número: ")
print(f"La suma de {num1} y {num2} es: {sumar(num1, num2)}")


# Conversión de Grados Celsius a Fahrenheit

def celsius_a_fahrenheit(celsius):

    return (celsius * 9/5) + 32


celsius = 25
print(f"{celsius} grados Celsius son {celsius_a_fahrenheit(celsius)} grados Fahrenheit.")


# Máximo de Tres Números

def maximo_de_tres(a, b, c):

    return max(a, b, c)

num1 = input("Digita el primer número: ")
num2 = input("Digita el segundo número: ")
num3 = input("Digita el tercer número: ")

print(f"El máximo de {num1}, {num2} y {num3} es: {maximo_de_tres(num1, num2, num3)}")


# Palíndromo

def es_palindromo(cadena):

    cadena = cadena.replace(" ", "").lower()  # Ignorar espacios y mayúsculas/minúsculas
    return cadena == cadena[::-1]

palabra = input("Digita una palabra: ")

print(f"¿'{palabra}' es un palíndromo? {es_palindromo(palabra)}")


# Factorial

def factorial(n):

    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

numero = input("Digita un número: ")
print(f"El factorial de {numero} es: {factorial(numero)}")


# Contar Vocales

def contar_vocales(cadena):

    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

cadena = input("Digita una oración: ")
print(f"La cadena '{cadena}' tiene {contar_vocales(cadena)} vocales.")

# Números Primos

def es_primo(n):

    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def numeros_primos(hasta):

    primos = []
    for num in range(2, hasta + 1):
        if es_primo(num):
            primos.append(num)
    return primos

limite = 20
print(f"Números primos hasta {limite}: {numeros_primos(limite)}")
