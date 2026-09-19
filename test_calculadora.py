from calculadora import calculator

def test_sums_2_numbers():
    assert calculator().suma(2, 3) == 5

def test_restas_2_numbers():
    assert calculator().resta(8, 3) == 5

def test_multiplicacion_2_numbers():
    assert calculator().multiplicacion(2, 4) == 8

def test_division_2_numbers():
    assert calculator().division(10, 2) == 5