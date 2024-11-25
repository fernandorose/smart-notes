import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, Dropout, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Aumentamos los datos de ejemplo
notas = [
    "Comprar leche", 
    "Idea para proyecto",
    "Ir al médico", 
    "Planificar la semana",
    "Reunión de trabajo",
    "Comprar regalos de cumpleaños",
    "Hacer ejercicios en el gimnasio",
    "Revisar correo electrónico",
    "Estudiar para examen",
    "Llamar a mamá",
    "Reunión con el equipo de desarrollo",
    "Llamar a los proveedores",
    "Organizar mi agenda",
    "Anotar tareas pendientes",
    "Escribir código para el proyecto",
    "Preparar informe mensual",
    "Comprar boletos de avión",
    "Revisar estado de proyectos"
]

# Etiquetas correspondientes (0: Tarea, 1: Idea, 2: Recordatorio, 3: Evento)
etiquetas = [0, 1, 2, 3, 1, 0, 0, 2, 0, 2, 3, 1, 0, 0, 1, 3, 2, 3]

# Tokenización y preprocesamiento de texto
tokenizer = Tokenizer(num_words=1000)
tokenizer.fit_on_texts(notas)
X = tokenizer.texts_to_sequences(notas)
X = pad_sequences(X, padding='post')

y = np.array(etiquetas)

# Crear el modelo de clasificación con mejoras
model = Sequential([
    Embedding(input_dim=1000, output_dim=64, input_length=X.shape[1]),
    Bidirectional(LSTM(64, return_sequences=True)),  # LSTM bidireccional
    Dropout(0.5),  # Dropout para evitar sobreajuste
    LSTM(64),  # Otra capa LSTM
    Dense(64, activation='relu'),
    Dense(4, activation='softmax')  # 4 categorías
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo con más épocas
model.fit(X, y, epochs=30, batch_size=4)

# Guardar el modelo
model.save('modelo_clasificacion.h5')
