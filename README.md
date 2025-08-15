# Pipeline de Dados IoT com Dashboard Streamlit

## Descrição do Projeto
Este projeto cria um pipeline de dados que processa leituras de temperatura de dispositivos IoT e armazena em um banco de dados PostgreSQL usando Docker. Além disso, inclui um dashboard interativo em Streamlit para visualização das métricas.

---

## Estrutura do Projeto

lucasmartinsbigdatafecaf/
├─ data/ # CSV do Kaggle
├─ sql/ # Views SQL salvas como .sql
├─ src/ # Scripts Python (ETL de ingestão)
├─ dashboard.py # Dashboard Streamlit
├─ requirements.txt # Lista de bibliotecas
├─ README.md # Documentação do projeto
├─ .gitignore # Arquivos ignorados pelo Git
└─ venv/ # Ambiente virtual (não subir para o GitHub)
├─ screenshots/ # Prints do dashboard

yaml
Copiar
Editar

---

## Configuração do Ambiente

1. **Instalar Python** (>=3.9)  
2. **Instalar Docker**  
3. **Criar ambiente virtual Python**

```bash
python -m venv venv
.\venv\Scripts\Activate   # Windows
Instalar bibliotecas necessárias

bash
Copiar
Editar
pip install --upgrade pip
pip install pandas sqlalchemy psycopg2-binary streamlit plotly python-dotenv
Gerar requirements.txt

bash
Copiar
Editar
pip freeze > requirements.txt
Banco de Dados
Criar contêiner PostgreSQL

bash
Copiar
Editar
docker run --name postgres-iot -e POSTGRES_PASSWORD=1234 -e POSTGRES_USER=postgres -e POSTGRES_DB=iotdb -p 5432:5432 -d postgres
Views SQL criadas

avg_temp_por_dispositivo → média de temperatura por dispositivo

leituras_por_hora → contagem de leituras por hora

temp_max_min_por_dia → temperaturas máxima e mínima por dia

Execução do ETL
Coloque o CSV do Kaggle dentro da pasta data/

Rodar o script de ingestão:

bash
Copiar
Editar
python src/ingest_iot.py
Dashboard Streamlit
Rodar o dashboard:

bash
Copiar
Editar
streamlit run dashboard.py
Abrir o navegador e acessar:

nginx
Copiar
Editar
Local URL: http://localhost:8501
Gráficos disponíveis:

Média de temperatura por dispositivo

Leituras por hora do dia

Temperaturas máximas e mínimas por dia

Prints do Dashboard
markdown
Copiar
Editar
![Média de Temperatura por Dispositivo](screenshots/Captura1.png)  
![Leituras por Hora do Dia](screenshots/Captura2.png)  
![Temperaturas Máximas e Mínimas por Dia](screenshots/Captura3.png)
Coloque os prints na pasta screenshots/ na raiz do projeto e renomeie como Captura1.png, Captura2.png e Captura3.png.

Possíveis Insights
Dispositivos com temperatura média mais alta

Horas do dia com maior número de leituras

Dias com maior variação de temperatura

Link do Dataset
Temperature Readings: IoT Devices – Kaggle

Autor
Nome: Lucaas011

GitHub: Lucaas011