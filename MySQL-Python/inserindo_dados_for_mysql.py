import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='cr7messiAB#$',
    database='relacionamento',
)

cursor = conexao.cursor()

# comando = (f'CREATE TABLE cliente (id_cliente INT PRIMARY KEY AUTO_INCREMENT NOT NULL, nome VARCHAR(30), idade INT, '
#            f'cidade VARCHAR(50), telefone VARCHAR(50))')
# cursor.execute(comando)
# conexao.commit()
# comando = (f'CREATE TABLE pedidos (id_pedido INT PRIMARY KEY AUTO_INCREMENT NOT NULL, total_pedido FLOAT, '
#            f'status VARCHAR(50), id_cliente INT NOT NULL, FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente))')
# cursor.execute(comando)
# conexao.commit()
# lista = ['"Diogo", 24, "Rio de Janeiro", "999999999"', '"João", 24, "Rio de Janeiro", "888888888"',
#          '"Júlia", 22, "São Paulo", "777777777"']
# for i in lista:
#     comando = (f'INSERT INTO cliente (nome, idade, cidade, telefone) '
#                f'VALUES ({i})')
#     cursor.execute(comando)
#     conexao.commit()
# lista2 = ['100, "Entregue", 1', '75, "Preparando", 2',
#           '85, "Pedido recebido", 3']
# for i in lista2:
#     comando = (f'INSERT INTO pedidos (total_pedido, status, id_cliente)'
#                f'VALUES ({i})')
#     cursor.execute(comando)
#     conexao.commit()

# comando = 'SELECT * FROM cliente'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(f'\033[31m{resultado}\033[m')

comando = 'SELECT * FROM pedidos'
cursor.execute(comando)
resultado = cursor.fetchall()
print(f'\033[32m{resultado}\033[m')

cursor.close()
conexao.close()
