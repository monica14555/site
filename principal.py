import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime
import os
from PIL import Image

# Configuração da página
# Carregar o ícone da página
icon_path = os.path.join("imagens", "foto dataconst.png")
if os.path.exists(icon_path):
    icon = Image.open(icon_path)
else:
    icon = "📊"

st.set_page_config(
    page_title="Dataconst Jr",
    page_icon=icon,
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS para traduzir o file uploader e centralizar títulos
st.markdown("""
    <style>
    /* Tradução do file uploader */
    .stFileUploader > div:first-child {
        color: transparent;
    }
    .stFileUploader > div:first-child::before {
        content: "Procurar arquivos";
        color: black;
    }
    .stFileUploader > div:first-child::after {
        content: "Arraste e solte o arquivo aqui";
        color: black;
    }
    
    /* Centralização de títulos */
    .centered-title {
        text-align: center !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar para seleção de tema
with st.sidebar:    
    # Logo da Dataconst Jr
    logo_path = os.path.join("imagens", "foto dataconst.png")
    if os.path.exists(logo_path):
        st.image(logo_path, width=200)
    else:
        st.image("https://via.placeholder.com/200x80?text=Dataconst+Jr", width=200)
    
    st.markdown("### Análises Confiáveis, Soluções Inteligentes")
    st.markdown("---")
    st.markdown('<h3 class="centered-title">Menu</h3>', unsafe_allow_html=True)
    page = st.radio(
        "Selecione uma opção:",
        ["🏠 Página Inicial", "📊 Análise Descritiva", "📈 Visualizações"]
    )
    st.markdown("---")
    st.markdown('<h3 class="centered-title">Alterar tema</h3>', unsafe_allow_html=True)
    st.markdown("💡 Para trocar de tema, vá no canto superior direito em ⋮ e em seguida em Settings/Configurações")

# Área principal
if page == "🏠 Página Inicial":
    # Cabeçalho
    st.markdown('<h1 class="centered-title">Bem-vindo à Dataconst Jr</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Seção de introdução
    col1, col2 = st.columns([1, 2])
    with col2:
        st.markdown("""
        <h3 class="centered-title">Sobre Nós</h3>
        A Dataconst Jr é a Empresa Júnior de Estatística da Universidade Federal da Bahia (UFBA), 
        especializada em dados e soluções estatísticas. Fundada por estudantes apaixonados por 
        estatística e tecnologia com o objetivo de aproximar a academia e o mercado de trabalho, contribuir positivamente 
        com a sociedade e proporcionar experiências práticas para os membros.

        Uma de nossas missões é democratizar o uso da estatística, oferecendo serviços de qualidade com preços acessíveis,
        desde modelagem preditiva até estudos de mercado, ajudamos a estruturar e interpretar informações de forma eficiente e impactante.
        Transformamos dados em insights estratégicos que impulsionam a tomada de decisões e geram valor para empresas, pesquisadores e organizações.

        Contamos com o suporte de professores experientes, garantindo entregas precisas e soluções personalizadas 
        para cada cliente. Na Dataconst Jr, acreditamos que cada dado conta uma história e estamos aqui para ajudá-lo a contá-la da 
        melhor forma possível.

        Entre em contato e descubra como podemos transformar seus dados!
        """, unsafe_allow_html=True)
    with col1:
        banner_path = os.path.join("imagens", "dataconst_jr.png")
        if os.path.exists(banner_path):
            st.image(banner_path, width=300)
        else:
            st.image("https://via.placeholder.com/300x200?text=Dataconst+Jr", width=300)
    
    # Serviços
    st.markdown('<h2 class="centered-title">Nossos Serviços</h2>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 🏛️ Serviços Acadêmicos
        - Análise de Iniciação Científica (IC) 🧪🥼 e Trabalho de Conclusão de Curso (TCC) 👨‍🎓
        - Análises para pesquisa de Mestrado ou Doutorado 📚
        """)
    
    with col2:
        st.markdown("""
        #### 💼 Serviços Empresariais
        - 🤖 Análise preditiva com Machine Learning e IA
        - 🖥 Elaboração de dashboards personalizados
        - 📑 Pesquisa de mercado/satisfação
        - 🏭✅ Controle de qualidade
        - 📂 Coleta, gerenciamento e organização de dados
        - 📉Construção e análise de indicadores
        """)
    
    with col3:
        st.markdown("""
        #### 📝 Outros serviços
        - 💡 Treinamentos e cursos 
        - 📋 Construção de questionários
        - 🌍 Análise espacial
        - 🗣👥 Grupo focal
        - 📊 Planejamento amostral
        - 🧪📏 Planejamento de experimentos
        """)
        
    st.markdown("""
    Em todos os projetos, a Dataconst Jr se compromete a oferecer suporte contínuo, garantindo a satisfação dos clientes 
    por meio de acompanhamento personalizado com excelência na entrega.
    """)

elif page == "📊 Análise Descritiva":
    st.markdown('<h1 class="centered-title">📊 Análise Descritiva</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Upload de dados
    uploaded_file = st.file_uploader("Carregue seus dados", type=['csv', 'xlsx', 'xls'])
    
    if uploaded_file is not None:
        try:
            # Leitura dos dados
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            # Informações básicas do dataset
            st.header("📋 Visão Geral dos Dados")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total de Registros", len(df))
            with col2:
                st.metric("Total de Colunas", len(df.columns))
            with col3:
                st.metric("Memória Utilizada", f"{df.memory_usage(deep=True).sum() / 1024:.2f} KB")
            
            # Visualização dos dados
            st.markdown("### Dados")
            st.dataframe(df.head())
            
            # Análise estatística
            st.header("📈 Análise Estatística")
            st.dataframe(df.describe())
            
        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {str(e)}")
    else:
        st.info("👆 Por favor, faça upload de um arquivo de dados para começar a análise.")

elif page == "📈 Visualizações":
    st.markdown('<h1 class="centered-title">📈 Visualizações de Dados</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Upload de dados
    uploaded_file = st.file_uploader("Carregue seus dados para visualização", type=['csv', 'xlsx', 'xls'])
    
    if uploaded_file is not None:
        try:
            # Leitura dos dados
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            # Tipos de visualização
            viz_type = st.selectbox(
                "Selecione o tipo de visualização",
                ["Gráfico de Dispersão", "Histograma", "Box Plot", "Linha do Tempo"]
            )
            
            if viz_type == "Gráfico de Dispersão":
                col1, col2 = st.columns(2)
                with col1:
                    x_axis = st.selectbox("Selecione a coluna para o eixo X", df.columns)
                with col2:
                    y_axis = st.selectbox("Selecione a coluna para o eixo Y", df.columns)
                
                fig = px.scatter(df, x=x_axis, y=y_axis, title=f"Relação entre {x_axis} e {y_axis}")
                st.plotly_chart(fig, use_container_width=True)
            
            elif viz_type == "Histograma":
                column = st.selectbox("Selecione a coluna para análise de distribuição", df.columns)
                fig = px.histogram(df, x=column, title=f"Distribuição de {column}")
                fig.update_layout(
                    yaxis_title="Contagem",
                    bargap=0.1,
                    bargroupgap=0.1,
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    xaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)'),
                    yaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
                )
                fig.update_traces(marker_color='#1f77b4')
                st.plotly_chart(fig, use_container_width=True)
            
            elif viz_type == "Box Plot":
                column = st.selectbox("Selecione a coluna para análise de outliers", df.columns)
                fig = px.box(df, y=column, title=f"Box Plot de {column}")
                fig.update_layout(
                    yaxis_title="Valores",
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    xaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)'),
                    yaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
                )
                fig.update_traces(marker_color='#1f77b4')
                st.plotly_chart(fig, use_container_width=True)
            
            elif viz_type == "Linha do Tempo":
                time_column = st.selectbox("Selecione a coluna de tempo", df.columns)
                value_column = st.selectbox("Selecione a coluna de valores", df.columns)
                fig = px.line(df, x=time_column, y=value_column, title=f"Evolução de {value_column} ao longo do tempo")
                st.plotly_chart(fig, use_container_width=True)
            
        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {str(e)}")
    else:
        st.info("👆 Por favor, faça upload de um arquivo de dados para criar visualizações.")

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido por Dataconst Jr - Empresa Júnior de Estatística da UFBA")

