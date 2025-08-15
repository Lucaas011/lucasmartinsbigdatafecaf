import pandas as pd
from sqlalchemy import create_engine
import os

# Configurações do banco (altere se necessário)
DB_USER = 'postgres'
DB_PASS = '123456'   # sua senha do docker postgres
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'iotdb'    # vamos usar um banco dedicado

# Caminho do CSV (ajustado para a pasta 'data' na raiz do projeto)
csv_path = "../data/archive/IOT-temp.csv"

if not os.path.exists(csv_path):
    raise FileNotFoundError(f"Arquivo não encontrado: {csv_path}")

# Ler o CSV
df = pd.read_csv(csv_path)

# Ajustar nomes das colunas para minúsculas
df.columns = [c.strip().lower() for c in df.columns]

# Renomear colunas para um padrão (baseado no CSV)
df.rename(columns={
    'id': 'log_id',
    'room_id/id': 'device_id',
    'noted_date': 'reading_time',
    'temp': 'temperature',
    'out/in': 'in_out'
}, inplace=True)

# Converter data/hora para formato datetime
df['reading_time'] = pd.to_datetime(df['reading_time'], errors='coerce', dayfirst=True)

# Converter temperatura para número
df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')

# Criar conexão com o banco
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Inserir no banco (cria ou substitui a tabela)
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("✅ Dados inseridos no banco com sucesso!")

