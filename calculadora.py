# calculadora.py

def sumar(a: float, b: float) -> float:
    return a + b

def restar(a: float, b: float) -> float:
    return a - b

def multiplicar(a: float, b: float) -> float:
    return a * b

def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b




def ejecutar_calculadora():
    operaciones = {
        "+": sumar,
        "-": restar,
        "*": multiplicar,
        "/": dividir,
   
    }

    print("Calculadora (escribe 'salir' para terminar)")
    while True:
        operacion = input("Operación (+, -, *, /): ").strip()
        if operacion.lower() == "salir":
            print("Hasta luego")
            return
        if operacion not in operaciones:
            print("Operación no válida")
            continue

        try:
            primer_numero = float(input("Primer número: "))
            segundo_numero = float(input("Segundo número: "))
            resultado = operaciones[operacion](primer_numero, segundo_numero)
        except ValueError as error:
            print(f"Error: {error}")
            continue

        print(f"Resultado: {resultado}")


if __name__ == "__main__":
    ejecutar_calculadora()
