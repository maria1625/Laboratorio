import unittest

from calculadora import dividir, multiplicar, restar, sumar


class CalculadoraTest(unittest.TestCase):
    def test_operaciones_basicas(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(restar(8, 3), 5)
        self.assertEqual(multiplicar(4, 3), 12)
        self.assertEqual(dividir(10, 2), 5)

    def test_division_entre_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)


if __name__ == "__main__":
    unittest.main()