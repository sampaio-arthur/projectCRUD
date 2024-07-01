import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

def atualizar_usuario():
    conexao = psycopg2.connect(user=DB_USER,
                               password=DB_PASSWORD,
                               host=DB_HOST,
                               port='5432',
                               database=DB_NAME)
    cursor = conexao.cursor()

    sql = 'UPDATE usuario SET nome = %s, sobrenome = %s, idade = %s WHERE id_usuario = %s'

    id_usuario = input('Digite o ID do usuário que você quer editar: ')
    nome = input('Digite o nome: ')
    sobrenome = input('Digite o sobrenome: ')
    idade = input('Digite a idade: ')

    dados = (nome, sobrenome, idade, id_usuario)

    cursor.execute(sql, dados)
    conexao.commit()

    atualizacao = cursor.rowcount
    print(f'Registro atualizado: {atualizacao}')

    cursor.close()
    conexao.close()
