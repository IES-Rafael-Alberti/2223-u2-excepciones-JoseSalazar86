import pytest
from src.Ejercicio2_3_1 import pideEdad,printMensaje

def test_pideEdad():
    pideEdad(5) == '1 2 3 4 5'
    assert pideEdad(10) == 10

def test_pideEdadNegativos():
    with pytest.raises(ValueError):
        pideEdad(-5) == "No vale numeros negativos"

#def test_printMensaje():
   # edad = pideEdad(edad)
    #printMensaje(10) == '\nSe han impreso los numeros del 1 al 10'
