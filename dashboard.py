import streamlit as st
import requests

API_URL = "http://localhost:8000"   # backend FastAPI

st.title("Dashboard - Streamlit + FastAPI")

st.write("Exemplo simples chamando a API FastAPI:")

if st.button("Chamar API"):
    r = requests.get(f"{API_URL}/hello")
    st.write("Resposta da API:", r.json())
