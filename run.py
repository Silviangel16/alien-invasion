from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta básica para la página principal
@app.route("/")
def home():
    return "¡Bienvenido a la versión web de Alien Invasion!"

# Ruta de ejemplo para manejar la lógica del juego
@app.route("/move", methods=["POST"])
def move():
    direction = request.json.get("direction")
    return jsonify({"message": f"Te moviste hacia {direction}"})
