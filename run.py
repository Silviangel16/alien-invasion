from flask import Flask, jsonify, request

app = Flask(__name__)

# Un ejemplo básico de ruta
@app.route("/")
def home():
    return "¡Bienvenido a la versión web de Alien Invasion!"

# Una ruta para manejar la lógica del juego (ejemplo)
@app.route("/move", methods=["POST"])
def move():
    direction = request.json.get("direction")
    return jsonify({"message": f"Te moviste hacia {direction}"})

if __name__ == "__main__":
    app.run(debug=True)
