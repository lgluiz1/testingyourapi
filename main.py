# testador.py
import streamlit as st
import requests


title = 'testing your api'

# Informações
tenant = ""  # Substitua pelo seu tenant (subdomínio)
token = ""  # Substitua pelo token gerado

st.title(f"{title}")

url = st.text_input("URL da API", "http://localhost:8000/ping")
headers = {
    'Content-Type': 'application/json',
    'X-Master-Key': ''  # Substitua pela sua chave de API
}

token = st.text_input("Do you have a token?")
parameters = st.text_input("Do you have parameters?")
payload = st.text_input("Do you have a payload?")


if st.button("Consultar"):
    try:
        # Cria um seletor se tive token
        if token : # Se tiver token
            headers = {
                        'Content-Type': 'application/json',
                        'X-Master-Key': f'{token}'  # Substitua pela sua chave de API
                    }
            # Fazendo a requisição GET
            response = requests.get(url, headers=headers)

        if payload: # Se tiver payload
            response = requests.post(url, json=payload)
            

        if token and payload: # Se tiver token e payload
            
            headers = {
                        'Content-Type': 'application/json',
                        'Authorization': f'Apikey {token}'  # Substitua pela sua chave de API
                    }
            payload = {"code": f"{payload}"}
            response = requests.post(url, headers=headers, json=payload)

        if parameters:
            response = requests.get(url, params=parameters)

        if not token and not parameters: # Se não tiver token
            response = requests.get(url)
        
        if token and parameters: # Se tiver token e parâmetros
            response = requests.get(url, headers=headers, params=parameters)
            
        st.write("Status Code:", response.status_code)
        st.json(response.json())
    except Exception as e:
        st.error(f"Erro ao fazer requisição: {e}")