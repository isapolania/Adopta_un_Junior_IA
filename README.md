<h1 align="center">Adopta_un_Junior_IA</h1>

# Proyecto prompt peliculas

[Haz clic aquí para ver el código](https://colab.research.google.com/drive/1U78nQwy0iNZo4dj08F7Y9ZH8RCbNBqCR#scrollTo=M6BQexJGQDrR)

## 📄Descripción  
El proyecto consiste en crear un prompt que recomiende películas.  
Esto se logra haciendo un llamado a la API de un LLM. En este caso, se realizó el llamado a la API de **Perplexity**, exactamente al modelo cuyo nombre es **sonar-pro**.

## 🚀 Características
- 🔗 Integración con API de Perplexity
- 🔐 Gestión segura de credenciales
- 🧠 Uso de modelos conversacionales
- 🎯 Prompt bien definido
- 🖨️ Salida directa del modelo
- 💻 Ejecutado en Google Colab

## 🛠️ Tecnologías utilizadas
  1. 🐍 Python
  2. 💻 Google Colab
  3. ☁️ Perplexity API
  4. 📦 openAI

## 🤖 Eficiencia del Prompt
Este prompt funciona porque es específico en el requerimiento, en el formato que necesita en la respuesta (JSON) y el modelo logró cumplir con lo que se quería. 
Además:
- Delimita claramente el contenido esperado, pidiendo exactamente 3 películas, lo que reduce la ambigüedad y evita respuestas demasiado extensas o vagas.
- Indica explícitamente el formato de salida (JSON), lo que guía al modelo hacia una estructura estándar, fácil de procesar y reutilizar.
- Restringe el output extra con la instrucción “No añadas texto adicional fuera del JSON”, lo cual evita introducciones, explicaciones innecesarias o firmas que el modelo suele agregar.

## 📥 Ejemplos de Entrada y Salida

| ENTRADA

Devuelve exactamente 3 películas en formato JSON.
Cada objeto debe incluir:
- "titulo": el nombre de la película,
- "genero": el género principal,
- "motivo": una frase breve que explique la razón de la recomendación.

No añadas texto adicional fuera del JSON.

| SALIDA 

📤 Salida - Ejemplo 1:

<img width="1849" height="429" alt="image" src="https://github.com/user-attachments/assets/4e29b32f-407b-459b-bb6b-006e4f7b29a7" />

📤 Salida - Ejemplo 2: 

<img width="1622" height="389" alt="image" src="https://github.com/user-attachments/assets/92d2f98d-e19d-4f68-8b7a-189bacd35c88" />





  
