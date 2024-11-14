"""
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 """

## Operadores aritméticos: +, -, *, /, %, **, //
## Para poder verificar si un número es par o impar, usaremos el operador módulo (%)
print("Vamos a verificar si es par o impar:")
numero = int(input("Ingresa el número:"))
if numero % 2 == 0:
    print("El número ingresado es par")
else:
    print("El número ingresado es impar")

## Division entera (//)
den = input("Ingresa el denominador:")
num = input("Ingresa el numerador:")

print("Este es el resultado de la división entera:", int(den) // int(num))

## Los demás son sencillos.

veces = int(input("Ingresa el numero de veces que quieres que se repita el mensaje:"))

for i in range(veces):
    print("Hello World")

##Ahora con While
vec = 0
while vec < 10:
    print("Hello World2")
    vec += 1

## Excepciones
try:
    result = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
