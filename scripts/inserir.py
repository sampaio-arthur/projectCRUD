import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

def inserir_usuario():
    conexao = psycopg2.connect(user=DB_USER,
                               password=DB_PASSWORD,
                               host=DB_HOST,
                               port='5432',
                               database=DB_NAME)
    cursor = conexao.cursor()

    sql = 'INSERT INTO usuario (nome, sobrenome, idade) VALUES(%s, %s, %s)'

    nome = input('Digite o seu nome: ')
    sobrenome = input('Digite o seu sobrenome: ')
    idade = input('Digite a sua idade: ')

    dados = (nome, sobrenome, idade)

    cursor.execute(sql, dados)
    conexao.commit()

    registros = cursor.rowcount
    print(f'Registro inserido: {registros}')

    cursor.close()
    conexao.close()
