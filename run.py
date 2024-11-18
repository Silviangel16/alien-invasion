from flask import Flask, render_template
import threading
import pygame
from alien_invasion import run_game

app = Flask(__name__)

# Ruta principal para la página web
@app.route("/")
def home():
    return "<h1>¡Bienvenido a Alien Invasion!</h1><p>Haz clic en el botón para iniciar el juego.</p><a href='/play'>Jugar</a>"

# Ruta para iniciar el juego
@app.route("/play")
def play():
    # Inicia el juego en un hilo diferente para evitar que bloquee el servidor Flask
    threading.Thread(target=run_game).start()
    return "<h1>El juego está corriendo</h1><p>Vuelve a la ventana del juego para jugar.</p>"

if __name__ == "__main__":
    app.run(debug=True)
