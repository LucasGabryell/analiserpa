import streamlit as st
import pandas as pd
import graphicsFunctions

# Título do aplicativo
st.title("Automações Maxicrédito")

# Substitua 'seu_arquivo.csv' pelo caminho real do seu arquivo CSV
dadosRpaCsv = 'dadosRPA.csv'

# Use o método 'read_csv' do pandas para ler o arquivo CSV
dadosRPA = pd.read_csv(dadosRpaCsv)

# Exibir os dados no Streamlit
st.write("### Dados do RPA:")
st.write(dadosRPA)

graphicsFunctions.display_automation_description(dadosRPA)

# Barra de seleção para escolher o gráfico
opcao_grafico = st.selectbox("Escolha o Gráfico", ["Gráfico de Tempo Manual",
                                                   "Gráfico de Tempo de execução RPA (Segundos)",
                                                   "Gráfico Manual Time X RPA Time", "Gráfico de Horas Retornadas"])

# Mostrar o gráfico selecionado com base na escolha do usuário
if opcao_grafico == "Gráfico de Tempo Manual":
    graphicsFunctions.plot_manual_time(dadosRPA)
elif opcao_grafico == "Gráfico de Tempo de execução RPA (Segundos)":
    graphicsFunctions.plot_rpa_time(dadosRPA)
elif opcao_grafico == "Gráfico Manual Time X RPA Time":
    graphicsFunctions.compare_manualtime_rpa_time(dadosRPA)
elif opcao_grafico == "Gráfico de Horas Retornadas":
    graphicsFunctions.plot_horas_retornadas(dadosRPA)
