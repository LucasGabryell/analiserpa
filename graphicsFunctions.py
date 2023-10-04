import streamlit as st
import plotly.express as px
import pandas as pd


def plot_manual_time(dados):
    # Adicione o filtro de Departamento com a opção "Todos"
    departamentos = ['Todos'] + list(dados['Department'].unique())
    departamento_selecionado = st.selectbox('Selecione um Departamento', departamentos)

    # Filtrar os dados com base no departamento selecionado, se não for "Todos"
    if departamento_selecionado != 'Todos':
        dados_filtrados = dados[dados['Department'] == departamento_selecionado]
        st.write(f"### Gráfico ManualTime para o Departamento: {departamento_selecionado}")
    else:
        dados_filtrados = dados
        st.write(f"### Gráfico ManualTime para Todos os Departamentos")

    # Agrupe os dados por ReleaseName e calcule a média do ManualTime
    media_manual_time = dados_filtrados.groupby('ReleaseName')['ManualTime'].mean().reset_index()

    # Crie o gráfico de barras
    fig = px.bar(media_manual_time, x='ReleaseName', y='ManualTime',
                 labels={'ReleaseName': 'Nome da Automação', 'ManualTime': 'Média Manual Time (segundos)'})

    st.plotly_chart(fig)

def plot_rpa_time(dados):
    # Adicione o filtro de Departamento com a opção "Todos"
    departamentos = ['Todos'] + list(dados['Department'].unique())
    departamento_selecionado = st.selectbox('Selecione um Departamento', departamentos)

    # Filtrar os dados com base no departamento selecionado, se não for "Todos"
    if departamento_selecionado != 'Todos':
        dados_filtrados = dados[dados['Department'] == departamento_selecionado]
        st.write(f"### Gráfico de Tempo de execução RPA para o Departamento: {departamento_selecionado}")
    else:
        dados_filtrados = dados
        st.write(f"### Gráfico de Tempo de execução RPA para Todos os Departamentos")

    # Agrupe os dados por ReleaseName e calcule a média do ManualTime
    media_manual_time = dados_filtrados.groupby('ReleaseName')['Tempo de execução RPA (Segundos)'].mean().reset_index()

    # Crie o gráfico de barras
    fig = px.bar(media_manual_time, x='ReleaseName', y='Tempo de execução RPA (Segundos)',
                 labels={'ReleaseName': 'Nome da Automação', 'Tempo de execução RPA (Segundos)': 'Média RPA Time (segundos)'})

    st.plotly_chart(fig)

def compare_manualtime_rpa_time(dados):
    # Adicione o filtro de Departamento com a opção "Todos"
    departamentos = ['Todos'] + list(dados['Department'].unique())
    departamento_selecionado = st.selectbox('Selecione um Departamento', departamentos)

    # Filtrar os dados com base no departamento selecionado, se não for "Todos"
    if departamento_selecionado != 'Todos':
        dados_filtrados = dados[dados['Department'] == departamento_selecionado]
        st.write(f"### Comparação entre ManualTime e Tempo de Execução RPA para o Departamento: {departamento_selecionado}")
    else:
        dados_filtrados = dados
        st.write(f"### Comparação entre ManualTime e Tempo de Execução RPA para Todos os Departamentos")

    # Calcula a média de ManualTime e RPA Time para cada ReleaseName
    media_manual_time = dados_filtrados.groupby('ReleaseName')['ManualTime'].mean().reset_index()
    media_rpa_time = dados_filtrados.groupby('ReleaseName')['Tempo de execução RPA (Segundos)'].mean().reset_index()

    # Une os dados de ManualTime e RPA Time com base em ReleaseName
    dados_comparacao = pd.merge(media_manual_time, media_rpa_time, on='ReleaseName', how='inner')

    # Renomeia as colunas
    dados_comparacao = dados_comparacao.rename(columns={'ManualTime': 'Média Manual Time (segundos)',
                                                      'Tempo de execução RPA (Segundos)': 'Média Tempo de Execução RPA (segundos)'})

    # Crie o gráfico de barras empilhadas
    fig = px.bar(dados_comparacao, x='ReleaseName', y=['Média Manual Time (segundos)', 'Média Tempo de Execução RPA (segundos)'],
                 labels={'ReleaseName': 'Nome da automação', 'value': 'Tempo Médio (segundos)'},
                 title='Comparação entre ManualTime e Tempo de Execução RPA',
                 barmode='group')

    st.plotly_chart(fig)

    # Calcule o tempo total utilizado manual e o tempo total utilizado RPA
    total_manual_time = dados_comparacao['Média Manual Time (segundos)'].sum()
    total_rpa_time = dados_comparacao['Média Tempo de Execução RPA (segundos)'].sum()

    # Exiba o tempo total em forma de texto
    st.write(f"Tempo Total Utilizado Manualmente: {total_manual_time:.2f} segundos")
    st.write(f"Tempo Total Utilizado com RPA: {total_rpa_time:.2f} segundos")
    st.write(f"Tempo Total otimizado com RPA: {total_manual_time - total_rpa_time:.2f} segundos")


def plot_horas_retornadas(dados):
    # Adicione o filtro de Departamento com a opção "Todos"
    departamentos = ['Todos'] + list(dados['Department'].unique())
    departamento_selecionado = st.selectbox('Selecione um Departamento', departamentos)

    # Filtrar os dados com base no departamento selecionado, se não for "Todos"
    if departamento_selecionado != 'Todos':
        dados_filtrados = dados[dados['Department'] == departamento_selecionado]
        st.write(f"### Horas Retornadas para o Departamento: {departamento_selecionado}")
    else:
        dados_filtrados = dados
        st.write(f"### Horas Retornadas para Todos os Departamentos")

    # Agrupe os dados por ReleaseName e calcule a soma das Horas Retornadas
    horas_retornadas = dados_filtrados.groupby('ReleaseName')['Horas Retornadas'].sum().reset_index()

    # Arredonde os valores para números inteiros
    horas_retornadas['Horas Retornadas'] = horas_retornadas['Horas Retornadas'].round().astype(int)

    # Crie o gráfico de barras empilhadas
    fig = px.bar(horas_retornadas, x='ReleaseName', y='Horas Retornadas',
                 labels={'ReleaseName': 'Noma da automação', 'Horas Retornadas': 'Horas Retornadas'},
                 title='Horas Retornadas',
                 text='Horas Retornadas')

    st.plotly_chart(fig)



def display_automation_description(dados):
    # Obtém a lista de ReleaseNames únicas e ordena em ordem alfabética
    release_names_ordenadas = sorted(dados['ReleaseName'].unique())

    # Adicione o filtro de ReleaseName
    release_selecionada = st.selectbox('Selecione uma automação', release_names_ordenadas)

    # Filtrar os dados com base na ReleaseName selecionada
    dados_filtrados = dados[dados['ReleaseName'] == release_selecionada]

    # Exibir a descrição da ReleaseName selecionada, se houver
    if not dados_filtrados.empty:
        descricao = dados_filtrados.iloc[0]['Descrição']
        st.write(f"Descrição da automação '{release_selecionada}':")
        st.write(descricao)
    else:
        st.write("Nenhuma descrição disponível para a automação selecionada.")

