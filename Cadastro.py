import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome,data_nasc,tipo):
    if nome and data_nasc <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome}, {data_nasc}, {tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False    

st.set_page_config(page_title="Cadastro de Clientes",
                   page_icon="📖")

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digite Seu Nome")

data_nasc = st.date_input("Data de Nascimento",
                          value=None, 
                          format="DD/MM/YYYY",
                          min_value= date(1900,1,1))

tipo = st.selectbox("Tipo do Cliente", 
                   ["Pessoa Júridica", "Pessoa Física"])

bt_cadastrar = st.button("Cadastrar",
          on_click=gravar_dados,
          args=[nome, data_nasc, tipo])

if bt_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente Cadastrado com sucesso",
                   icon="✅")
    else:
        st.error("Ocorreu Algum Problema no Cadastro!",
                 icon="❌")    

