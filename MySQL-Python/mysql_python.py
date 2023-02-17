import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='cr7messiAB#$',
    database='words',
)

cursor = conexao.cursor()

palavra = "Timber = madeira"

id = 84

# comando = f'INSERT INTO palavras (ID) VALUES ({id})' # Criando uma linha nova de acordo com o ID

comando = f'UPDATE palavras SET T = "{palavra}" WHERE ID = {id}'
cursor.execute(comando)
conexao.commit()
# resultado = cursor.fetchall()

cursor.close()
conexao.close()

# CRUD:

# CREATE:
# palavra = "Secedes = separa"
# id = 229
# comando = f'INSERT INTO words (palavra, id) VALUES ("{palavra}", {id})'
# cursor.execute(comando)
# conexao.commit()  # Quando edita o Banco de dados

# READ:
# comando = 'SELECT * FROM words'
# cursor.execute(comando)
# resultado = cursor.fetchall()  # Ler o Banco de dados
# print(resultado)

# UPDATE:
# palavra = "Secedes = separa"
# id = 229
# comando = f'INSERT INTO palavras (ID) VALUES ({id})' # Criando uma linha nova de acordo com o ID
# comando = f'UPDATE palavras SET S = "{palavra}" WHERE ID = {id}'
# cursor.execute(comando)
# conexao.commit()
# conexao.commit()  # Quando edita o Banco de dados

# DELETE:
# palavra = "Secedes = separa"
# comando = f'DELETE FROM words WHERE palavra = "{palavra}"'
# cursor.execute(comando)
# conexao.commit()  # Quando edita o Banco de dados
