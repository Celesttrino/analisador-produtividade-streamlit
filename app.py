import pandas as pd
import streamlit as st

# Configura o título e o ícone na página do navegador
st.set_page_config(page_title="Dashbord de Estudos", page_icon="📊")

# Título principal da página web
st.title("📊 Painel de produtibidade do Aluno")
st.markdown("Bem-vindo ao seu sistema de acompanhamento de estudos interativo.")

#1.  Carregar dados
# Cria um botão de upload na barra lateral esquerda
arquivo_usuario = st.sidebar.file_uploader("Escolha seu arquivo CSV", type=["csv"])
# se o cliente enviou o arquivo(ou seja, não está vazio)
if arquivo_usuario is not None: 
    df = pd.read_csv(arquivo_usuario)
else:
    #se estiver vazio, roda o arquivo teste
    df = pd.read_csv('produtividade.csv')


#2. Criar a seção de estatíscas na tela
st.subheader("📈 Resumo do progresso")

# Exibe os números em formato de cartões bonitos (Métricas)
total_horas = df['horas_estudo'].sum()
media_horas = df['horas_estudo'].mean()
total_projetos = df["projetos_concluidos"].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total de horas", f"{total_horas}h")
col2.metric("Média diária", f"{media_horas}h")
col3.metric("Projetos concluídos", total_projetos)

#3. Criar o gráfico interativo
st.subheader("📅 Evolução das horas de estudo diárias")
# O streamlit cria um gráfico de linhas com apenas uma linha de código
st.line_chart(data=df, x='data', y='horas_estudo')

#4. Mostrar a tebela de dados pro cliente conferir
st.subheader("📋 Visualizar dados completos")
st.dataframe(df)