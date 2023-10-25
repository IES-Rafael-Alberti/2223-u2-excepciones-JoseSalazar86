'''
jercicio 2.3.2¶

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''
def numeroImpares(numero:int):
    if numero < 0 :
        raise ValueError("Tiene que ser numeros positivos.")
    for i in range(1,numero,2):
        print(i,end=",")
    return numero

if __name__ == "__main__":
    try:
        numero = int(input("Introduce un numero: "))

        contImpares = numeroImpares(numero)

        print(contImpares)

    except ValueError:
        print("No es un numero lo que has introducido")

  