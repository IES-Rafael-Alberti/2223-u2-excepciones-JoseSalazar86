'''
Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
 Deberá solicitar el número hasta introducir uno correcto. 
'''
def cuentaAtras(numero:int):
    if numero < 0 :
        raise ValueError("Introduce un numero positivo")
    for i in range(numero,-1,-1):
            print(i,end=", ")
    return numero
    
if __name__ == "__main__":
    try:
        numero = int(input("Introduce un numero: "))

        contAtras = cuentaAtras(numero)

        print(contAtras)

    except ValueError:
         print("no es un numero")