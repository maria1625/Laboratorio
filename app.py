import os
from flask import Flask, request, jsonify
from calculadora import sumar, restar, multiplicar, dividir, potencia


app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "calculadora-api",
        "commit": os.getenv("RENDER_GIT_COMMIT", "local")
    }), 200



# 3. Endpoint para ejecutar las operaciones de la calculadora
@app.route("/calcular", methods=["GET"])
def operar():
    op = request.args.get("op", "suma")
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))

        if op == "suma":
            res = sumar(a, b)
        elif op == "resta":
            res = restar(a, b)
        elif op == "mult":
            res = multiplicar(a, b)
        elif op == "division":
            res = dividir(a, b)
        
        else:
            return jsonify({"error": "Operación no válida"}), 400

        return jsonify({"operacion": op, "a": a, "b": b, "resultado": res}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)