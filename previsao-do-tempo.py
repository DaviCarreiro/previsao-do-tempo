import streamlit as st
import requests
from datetime import datetime

API_KEY = "5f41f7900da9b4bde1311f763ea12e96"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

st.set_page_config(page_title="Previsão do Tempo", layout="centered")
st.title("☁️ Previsão do Tempo")

cidade = st.text_input("Digite o nome da cidade:")

if cidade:
    dados = get_weather(cidade)
    if dados:
        st.subheader(f"Clima em {cidade.title()}")
        st.metric("Temperatura", f"{dados['main']['temp']} °C")
        st.write("Descrição:", dados['weather'][0]['description'].title())
        st.write("Umidade:", f"{dados['main']['humidity']}%")
        st.write("Vento:", f"{dados['wind']['speed']} m/s")
        st.write("Atualizado em:", datetime.fromtimestamp(dados['dt']).strftime("%d/%m/%Y %H:%M"))
    else:
        st.error("Cidade não encontrada ou erro na API.")