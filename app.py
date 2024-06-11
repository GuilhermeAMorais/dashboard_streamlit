import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import numpy as np

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Adicionando dados
data = {
    'Regiao': ['Norte', 'Sul', 'Leste', 'Oeste'],
    'Vendas': [35000, 28000, 40000, 32000],
    'vendedores': ['João', 'Ana', 'Marcelo', 'Pedro']
}
df = pd.DataFrame(data)

st.title("O Dashboard.") 

def display_dataframe(df):
    st.header("Visualização do Dataframe")
    logging.info("Visualização do Dataframe iniciada")

    st.sidebar.header("Filtros")
    selected_region = st.sidebar.multiselect(
        "Selecione as regiões.",
        df['Regiao'].unique(),
        df['Regiao'].unique()
    )
    logging.info(f"Regiões selecionadas para filtro: {selected_region}")

    filtered_data = df[df['Regiao'].isin(selected_region)]
    st.write(filtered_data)
    logging.info("Dataframe filtrado exibido")
  
def display_charts(df):
    st.header("Visualização de Gráficos")
    logging.info("Visualização de Gráficos iniciada")

    st.subheader("Desempenho por região.")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Regiao', y='Vendas', data=df, ax=ax)
    plt.xlabel('Região')
    plt.ylabel('Vendas')
    plt.title('Vendas por Região')
    st.pyplot(fig)
    logging.info("Gráfico de vendas por região exibido")

#Função para exibir métricas     
def display_metrics(df):
        st.subheader("Métricas")
        
        #métricas simples
        total_sales = df['Vendas'].sum()
        average_sales = df['Vendas'].mean()
        most_productive = df['vendedores'].value_counts().idxmax()
        
        coluna1, coluna2, coluna3 = st.columns(3)
        with coluna1:
            st.metric("O vendedor mais produtivo foi:", most_productive)
            
        with coluna2:
            st.metric('Vendas totais:', total_sales)
            
        with coluna3:
            st.metric('Preço médio:', round(average_sales, 2))
  
def main():
    st.title("Dashboard de Vendas :shopping_trolley:")
    logging.info("Título do dashboard definido")

    aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
    logging.info("Abas do dashboard criadas: Dataset, Receita, Vendedores")

    with aba1:
        display_dataframe(df)
    with aba2:
        display_charts(df)
    with aba3:
        display_metrics(df)
                  
if __name__ == "__main__":
    main()
    logging.info("Aplicação iniciada")
