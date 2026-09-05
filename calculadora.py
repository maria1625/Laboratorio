"""Calculadora sencilla para usar desde consola o como módulo."""


def sumar(primer_numero, segundo_numero):
    return primer_numero + segundo_numero


def restar(primer_numero, segundo_numero):
    return primer_numero - segundo_numero


def multiplicar(primer_numero, segundo_numero):
    return primer_numero * segundo_numero


def dividir(primer_numero, segundo_numero):
    if segundo_numero == 0:
        raise ValueError("No se puede dividir entre cero")
    return primer_numero / segundo_numero


def ejecutar_calculadora():
    operaciones = {
        "+": sumar,
        "-": restar,
        "*": multiplicar,
        "/": dividir,
    }

    print("Calculadora sencilla (escribe 'salir' para terminar)")
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