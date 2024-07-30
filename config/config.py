import os
from dotenv import load_dotenv

# Carregue as variáveis do arquivo .env
load_dotenv()

# Configurações do banco de dados
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
