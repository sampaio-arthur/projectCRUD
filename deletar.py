import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

def deletar_usuario():
    conexao = psycopg2.connect(user=DB_USER,
                               password=DB_PASSWORD,
                               host=DB_HOST,
                               port='5432',
                               database=DB_NAME)
    cursor = conexao.cursor()

    sql = 'DELETE FROM usuario WHERE id_usuario = %s'
    id_usuario = input('Digite o ID do usuario que você quer excluir: ')

    cursor.execute(sql, (id_usuario,))
    conexao.commit()

    registro_eliminado = cursor.rowcount
    print(f'Registros eliminados: {registro_eliminado}')

    cursor.close()
    conexao.close()
