from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Opciones válidas del juego
OPCIONES = ["piedra", "papel", "tijera"]

@app.route('/')
def index():
    # Carga la página principal del juego
    return render_template('index.html')

@app.route('/jugar', methods=['POST'])
def jugar():
    # Recibimos la elección del usuario desde el frontend (JSON)
    datos = request.get_json()
    usuario = datos.get('eleccion')
    
    if usuario not in OPCIONES:
        return jsonify({'error': 'Opción no válida'}), 400

    # La computadora elige al azar
    computadora = random.choice(OPCIONES)
    
    # Lógica para determinar el resultado
    if usuario == computadora:
        resultado = "¡Es un empate! 🤝"
    elif ... :
        resultado = "¡GANASTE! 🎉🏆"
    else:
        resultado = "Perdiste... 🤖💀"

    return jsonify({
        'usuario': usuario,
        'computadora': computadora,
        'resultado': resultado
    })

if __name__ == '__main__':
    app.run(debug=True)