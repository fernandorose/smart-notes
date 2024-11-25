<div align="center">
	<h1>SmartNote</h1>
	<p>
		<b></b>
	</p>
	<br>
</div>

**SmartNote** es una aplicación simple de notas desarrollada con **AstroJS** que utiliza una red neuronal para clasificar el contenido de las notas en tiempo real mediante **WebSockets** y un servidor Flask.

---

## 🚀 Funcionalidades

- **Edición en línea:** Los usuarios pueden escribir notas en un contenedor editable.
- **Clasificación con IA:** Clasifica el contenido de las notas en tiempo real mediante un modelo de inteligencia artificial.
- **WebSocket integrado:** Comunicación en tiempo real con un backend Flask para la clasificación de texto.

---

## 📦 Estructura del proyecto

- Aplicacion web

```plaintext
/
├── components/
│   └── Layout.astro       # Componente de diseño general
├── pages/
│   └── index.astro        # Página principal de la aplicación
├── public/
│   └── favicon.ico        # Ícono del proyecto
├── styles/
│   └── globals.css        # Estilos globales del proyecto
├── README.md              # Documentación del proyecto
└── package.json           # Dependencias del proyecto
```

- Api y modelo con python

```plaintext
/
├── venv/
├── main.py                    # Aplicacion principal (api)
├── model.py                   # Modelo de clasificacion
├── requeriments.py            # Dependencias
└── modelo_clasificacion.h5    # Modelo guardado
```

---

## 🛠️ Tecnologías usadas

- **Frontend:**

  - [AstroJS](https://astro.build/)
  - HTML5 & CSS3
  - TypeScript

- **Backend:**

  - [Flask](https://flask.palletsprojects.com/)
  - WebSocket con [Socket.IO](https://socket.io/)

- **Clasificación con IA:**
  - Red neuronal personalizada implementada en el servidor Flask.

---

## ⚙️ Configuración del proyecto

### **Requisitos previos**

- Node.js >= 16
- Python >= 3.8
- Servidor Flask con modelo de IA configurado (en `localhost:5000`)

### **Instalación**

1. **Clona este repositorio:**

   ```bash
   git clone https://github.com/fernandorose/smart-notes.git
   cd smartnote
   ```

2. **Instala las dependencias:**

- Crear el entorno de python

```bash
cd api
```

```bash
python -m venv venv
```

- Activar el entorno

```bash
.\venv\Scripts\activate
```

- Instalar las dependencias de pip del archivo requirements.txt

```bash
pip install -r requirements.txt
```

- Instalar dependencias de astroJS

```bash
cd client
```

```bash
npm install
```

3. **Configura el servidor Flask:**

   - Asegúrate de que el servidor Flask esté corriendo en `http://localhost:5000`

4. **Inicia la aplicación:**

- Ejecutar la api con el entorno venv activado

  ```bash
  cd api
  python main.py
  ```

- Ejecutar la app web

  ```bash
  cd client
  npm run dev
  ```

  La aplicación estará disponible en `http://localhost:3000`.

---

## 💻 Uso

1. Escribe una nota en el área de texto editable.
2. Observa cómo la nota es clasificada automáticamente en tiempo real.
3. La categoría se muestra en la sección de clasificación.

---

## 📂 Archivos clave

- **`pages/index.astro`**: Contiene la implementación principal del editor de notas y la integración con WebSocket.
- **`styles/globals.css`**: Define el diseño visual de la aplicación.
- **Servidor Flask (no incluido):** Debe manejar el evento `clasificar_nota` para procesar las notas y devolver la clasificación.

---

## 📄 Licencia

Este proyecto está bajo la licencia [MIT](./LICENSE). Puedes usarlo, modificarlo y distribuirlo según los términos de la licencia.
