import pytest
from   src.Ejercicio2_3_3 import cuentaAtras

def test_cuentaAtras():
    cuentaAtras(10) == 10

def test_cuentaAtrasNegativos():
   with pytest.raises(ValueError):
    cuentaAtras(-5) == "Introduce un numero positivo"