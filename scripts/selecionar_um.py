import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

def selecionar_um():
    conexao = psycopg2.connect(user=DB_USER,
                               password=DB_PASSWORD,
                               host=DB_HOST,
                               port='5432',
                               database=DB_NAME)
    cursor = conexao.cursor()

    sql = 'SELECT * FROM usuario WHERE id_usuario = %s'
    id_usuario = input('Digite o ID do usuário: ')

    cursor.execute(sql, (id_usuario,))
    registro = cursor.fetchone()

    if registro:
        print(registro)
    else:
        print('Usuário não encontrado.')

    cursor.close()
    conexao.close()
