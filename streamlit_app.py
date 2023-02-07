import streamlit as st
import openai

# Configurar la API de OpenAI
openai.api_key = "YOUR_OPENAI_API_KEY"

# Mostrar un formulario con las preguntas para el usuario
st.title("Generador de plan de negocios")
business_idea = st.text_input("¿Cuál es su idea de negocio?")
initial_capital = st.text_input("¿De qué capital inicial dispone?")

# Generar un plan de negocios utilizando la API de OpenAI
if business_idea and initial_capital:
    response = openai.Completion.create(
        engine="text-davinci-03",
        prompt="A partir de mi idea de negocio " + business_idea + " y con un capital inicial de " + initial_capital + ", ¿podría generar un plan de negocios para mí?",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    # Mostrar el plan de negocios generado por OpenAI
    st.write("Aquí está su plan de negocios generado por OpenAI:")
    st.write(response)
