import pytest
from src.Ejercicio2_3_2 import numeroImpares

def test_numeroImpares():

    numeroImpares(10) == '1,3,5,7,9,10'

def test_numeroImparesNegativos():
   with pytest.raises(ValueError):
    numeroImpares(-5) == "Tiene que ser numeros positivos."