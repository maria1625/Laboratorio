from calculadora import calculator

def test_sums_2_numbers():
    assert calculator().suma(2, 3) == 5

def test_restas_2_numbers():
    assert calculator().resta(8, 3) == 5