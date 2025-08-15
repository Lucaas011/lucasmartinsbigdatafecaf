import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# ---------- CONFIGURAÇÃO DO BANCO ----------
DB_USER = 'postgres'
DB_PASS = '123456'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'iotdb'

# Conexão com PostgreSQL
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# ---------- FUNÇÃO PARA LER VIEWS ----------
@st.cache_data
def carregar_view(query):
    return pd.read_sql(query, engine)

# ---------- TÍTULO DO DASHBOARD ----------
st.title("Dashboard IoT - Temperaturas")

# ---------- Gráfico 1: Média de temperatura por dispositivo ----------
st.subheader("Média de Temperatura por Dispositivo")
df_avg = carregar_view("SELECT * FROM avg_temp_por_dispositivo;")
st.dataframe(df_avg)
st.bar_chart(df_avg.set_index('device_id')['avg_temp'])

# ---------- Gráfico 2: Leituras por hora ----------
st.subheader("Número de Leituras por Hora")
df_hour = carregar_view("SELECT * FROM leituras_por_hora;")
st.dataframe(df_hour)
st.bar_chart(df_hour.set_index('hora')['contagem'])

# ---------- Gráfico 3: Temperaturas máximas e mínimas por dia ----------
st.subheader("Temperaturas Máximas e Mínimas por Dia")
df_temp = carregar_view("SELECT * FROM temp_max_min_por_dia;")
st.dataframe(df_temp)
st.line_chart(df_temp.set_index('data')[['temp_max', 'temp_min']])
