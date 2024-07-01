import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

def selecionar_todos():
    conexao = psycopg2.connect(user=DB_USER,
                               password=DB_PASSWORD,
                               host=DB_HOST,
                               port='5432',
                               database=DB_NAME)
    cursor = conexao.cursor()

    sql = 'SELECT * FROM usuario'

    cursor.execute(sql)
    registros = cursor.fetchall()

    for linha in registros:
        print(linha)

    cursor.close()
    conexao.close()
