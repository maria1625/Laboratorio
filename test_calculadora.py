# test_calculadora.py
import pytest
from calculadora import sumar, restar, multiplicar, dividir, potencia

def test_operaciones_basicas():
    assert sumar(10, 5) == 15
    assert restar(10, 5) == 5
    assert multiplicar(4, 3) == 12
    assert dividir(20, 4) == 5

# TEST CRÍTICO 1: Prevenir caída del sistema por división entre cero (Fail-fast)
def test_critico_division_por_cero():
    with pytest.raises(ValueError, match="No se puede dividir entre cero"):
        dividir(10, 0)

# TEST CRÍTICO 2: Precisión con números negativos y decimales en operaciones encadenadas
def test_critico_operaciones_con_negativos_y_decimales():
    assert multiplicar(-2.5, 4) == -10.0
    assert sumar(-10.0, 2.5) == -7.5
    assert potencia(2, 3) == 8
