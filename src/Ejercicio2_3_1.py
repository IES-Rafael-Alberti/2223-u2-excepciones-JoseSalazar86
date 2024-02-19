'''
Ejercicio 2.3.1

Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''

'''
def pideEdad(edad:int):
numeros =[]
    if edad < 0 :
        raise ValueError("No vale numeros negativos")
    for i in range(1,edad +1):
        numeros.append(i)
    return numeros

'''
def pideEdad(edad:int):
    if edad < 0 :
        raise ValueError("No vale numeros negativos")
    for i in range(1,edad +1):
        print(i, end=" ")
    return edad

def printMensaje(total:int) -> str:
    total = pideEdad(edad)
    return f"\nSe han impreso los números del 1 al {total}"


if __name__ == "__main__":
    try:
        edad = int (input("Introduce tu edad: "))
         
        total = pideEdad(edad)
        mensaje = printMensaje(total)
        printMensaje(total)
    
    except ValueError:
        print("No es un numero lo que has introducido.")
    

