# Pipeline de Dados IoT com Dashboard Streamlit

## Descrição
Projeto que processa leituras de temperatura de dispositivos IoT e armazena em PostgreSQL via Docker. Inclui dashboard interativo em Streamlit para visualização de métricas.

## Estrutura do Projeto
lucasmartinsbigdatafecaf/
├─ data/ # CSV do Kaggle
├─ sql/ # Views SQL
├─ src/ # Scripts Python (ETL)
├─ dashboard.py # Dashboard Streamlit
├─ requirements.txt # Bibliotecas necessárias
├─ README.md # Este arquivo
├─ screenshots.pdf # Capturas do dashboard
└─ venv/ # Ambiente virtual (não subir para o GitHub)

r
Copiar
Editar

## Configuração do Ambiente
1. Criar e ativar ambiente virtual:
```bash
python -m venv venv
.\venv\Scripts\Activate   # Windows
Instalar bibliotecas:

bash
Copiar
Editar
pip install --upgrade pip
pip install -r requirements.txt
Banco de Dados
Criar contêiner PostgreSQL:

bash
Copiar
Editar
docker run --name postgres-iot -e POSTGRES_PASSWORD=1234 -e POSTGRES_USER=postgres -e POSTGRES_DB=iotdb -p 5432:5432 -d postgres
Execução
Rodar ETL:

bash
Copiar
Editar
python src/ingest_iot.py
Rodar dashboard:

bash
Copiar
Editar
streamlit run dashboard.py
Acesse: http://localhost:8501

Prints do Dashboard
Todas as capturas estão em screenshots.pdf.

Autor
Lucas Martins (GitHub: Lucaas011)

:-)