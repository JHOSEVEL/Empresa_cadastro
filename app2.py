import openpyxl 
import streamlit as st  # nesta linha o streamlit e import
import pandas as pd


st.title("Cadastre sua Empresa") # titulo 


nome = st.text_input("Digite o nome da Empresa") #input  nome da empresa

cnpj = st.text_input("insira o cnpj da empresa")# input cnpj

endereco = st.text_input("Digite o Endereço da Empresa")

email = st.text_input("Digite o email da Empresa")

area = st.text_input("Digite a area de atuação da Empresa")# entrada de area de negocio da empresa
soft_skills = st.text_input("Quais soft skills o candidato precisa ter?")

data = st.date_input("insira a data de cadastro")

cadastro = st.button("cadastrar cliente") #botão enviar cadastro

if cadastro: # Torna o click do botão verdade e o aciona
    with open("base_dados.csv","a") as arquivo: # abre o arquivo que sera a base de dados
        arquivo.write(f"{nome},{cnpj},{endereco},{email},{area},{soft_skills}\n") # escreve no arquivo o que foi colocado no formulario
        st.success("cliente cadastrado com sucesso") # envia uma mensagem de sucesso informando que o codigo funcionou