# app.py

import openai
import streamlit as st

# Configura tu clave API de OpenAI
openai.api_key = 'tu-clave-api'

# Crea la interfaz de usuario
st.title('ChatGPT')
input_text = st.text_input('Escribe tu mensaje:')
if st.button('Enviar'):
    if input_text:
        # Utiliza la API de GPT-3 para generar una respuesta
        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=input_text,
          max_tokens=150
        )
        st.write(response.choices[0].text.strip())
    else:
        st.write('Por favor, escribe un mensaje.')
