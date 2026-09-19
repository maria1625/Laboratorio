class calculator:
    
    def suma(self, a:int, b:int) -> int:
        return a + b
    
    def resta(self, a:int, b:int) -> int:
        return a - b

    def multiplicacion(self, a:int, b:int) -> int:
        return a * b

    def division(self, a:float, b:float) -> float:
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b