# Pipeline de Dados IoT com Dashboard Streamlit

## Descrição
Este projeto processa leituras de temperatura de dispositivos IoT, armazena em PostgreSQL via Docker e apresenta um dashboard interativo com Streamlit.

## Estrutura do Projeto
lucasmartinsbigdatafecaf/

├─ data/ # CSV do Kaggle

├─ sql/ # Views SQL (.sql)

├─ src/ # Scripts Python (ETL)

│ └─ screenshots/ # Prints do dashboard

├─ dashboard.py # Dashboard Streamlit

├─ requirements.txt # Bibliotecas

├─ README.md # Documentação

└─ .gitignore # Arquivos ignorados


## Configuração do Ambiente
1. Criar ambiente virtual:
```bash
python -m venv venv
.\venv\Scripts\Activate   # Windows
Instalar bibliotecas:

bash
pip install --upgrade pip
pip install pandas sqlalchemy psycopg2-binary streamlit plotly python-dotenv
pip freeze > requirements.txt
Criar contêiner PostgreSQL:

bash
docker run --name postgres-iot -e POSTGRES_PASSWORD=1234 -e POSTGRES_USER=postgres -e POSTGRES_DB=iotdb -p 5432:5432 -d postgres
Execução
Colocar CSV do Kaggle em data/

Rodar ETL:

bash
python src/ingest_iot.py
Rodar dashboard:

bash
streamlit run dashboard.py
Local URL: http://localhost:8501

Prints do Dashboard
Os prints estão disponíveis na pasta src/screenshots/.

Possíveis Insights
Dispositivos com temperatura média mais alta

Horas do dia com maior número de leituras

Dias com maior variação de temperatura

Autor
GitHub: Lucaas011