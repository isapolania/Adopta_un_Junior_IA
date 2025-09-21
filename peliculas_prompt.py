import openai
from google.colab import userdata
import re

# Llamar la función OpenAI de Perplexity
client = openai.OpenAI(
    api_key=userdata.get('PERPLEXITY_API_KEY'),
    base_url="https://api.perplexity.ai"
)

PROMPT = """'Devuelve exactamente 3 películas en formato JSON.
Cada objeto debe incluir:
- "titulo": el nombre de la película,
- "genero": el género principal,
- "motivo": una frase breve que explique la razón de la recomendación.

No añadas texto adicional fuera del JSON.'
"""

# Solicitar la respuesta al modelo sonar-pro
response = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": PROMPT}],
)

# Función para eliminar referencias
def limpiar_referencias(texto):
    return re.sub(r'\[\d+\]', '', texto)

# Obtener resultados
contenido = response.choices[0].message.content
#Eliminar el contenido de referencias 
contenido_limpio = limpiar_referencias(contenido)

# Guardar en archivo .json
with open("peliculas.json", "w", encoding="utf-8") as f:
    json.dump(contenido_limpio, f, ensure_ascii=False, indent=4)

# Mostrar resultado modificado
print(contenido_limpio)
