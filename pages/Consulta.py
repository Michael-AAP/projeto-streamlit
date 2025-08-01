import streamlit as st
import pandas as pd

st.title("Consulta de Clientes Cadastrados")
st.divider()

dados = pd.read_csv("clientes.csv")

st.dataframe(dados, hide_index=True)