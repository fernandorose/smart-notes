from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import tensorflow as tf
import numpy as np
from flask_cors import CORS  # Importamos CORS

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar WebSocket
socketio = SocketIO(app, cors_allowed_origins="http://localhost:4321")  # Permite WebSocket desde localhost:4321

# Habilitar CORS solo para http://localhost:4321
CORS(app, resources={r"/*": {"origins": "http://localhost:4321"}})

# Configuración de cabeceras CORS
app.config['CORS_HEADERS'] = 'Content-Type'

# Cargar el modelo de clasificación
modelo = tf.keras.models.load_model("modelo_clasificacion.h5")  # Ruta al modelo guardado

# Definir un evento para WebSocket
@socketio.on('clasificar_nota')
def clasificar_nota(data):
    try:
        # Obtener los datos del cliente
        datos = data.get("nota", "")
        if not datos:
            emit('error', {"error": "La nota está vacía"})
            return

        # Preprocesar la nota (ejemplo básico: convertir en vectores numéricos)
        vector = np.array([len(datos), datos.count(" ")])  # Ejemplo básico
        vector = np.expand_dims(vector, axis=0)  # Añadir dimensión para el modelo

        # Hacer la predicción
        prediccion = modelo.predict(vector)
        categoria = np.argmax(prediccion)

        # Definir los nombres de las categorías
        categorias = {0: "Tarea", 1: "Idea", 2: "Recordatorio", 3: "Evento"}

        # Responder con el nombre de la categoría y confianza
        emit('resultado_clasificacion', {
            "categoria": categorias[categoria],
            "confianza": prediccion.tolist()
        })

    except Exception as e:
        emit('error', {"error": str(e)})


if __name__ == "__main__":
    # Ejecutar el servidor Flask con WebSocket
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)  # Asegúrate de que sea accesible
