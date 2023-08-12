import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='cr7messiAB#$',
    database='integracao',
)

cursor = conexao.cursor()

# comando = f'CREATE TABLE pessoas (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, nome VARCHAR(40), idade INT)'
# cursor.execute(comando)
# conexao.commit()

# comando = (f'CREATE TABLE celulares (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, marca VARCHAR(20) NOT NULL, '
#            f'modelo VARCHAR(20), celular_pes INT NOT NULL, FOREIGN KEY (celular_pes) REFERENCES pessoas(id))')
# cursor.execute(comando)
# conexao.commit()

# comando = (f'INSERT INTO pessoas(nome, idade) '
#            f'VALUES'
#            f'("Diogo", 24),'
#            f'("João", 24),'
#            f'("Júlia", 22),'
#            f'("Alice", 26)')
# cursor.execute(comando)
# conexao.commit()

comando = (f'INSERT INTO celulares (marca, modelo, celular_pes) '
           f'VALUES'
           f'("Apple", "8 plus", 1),'
           f'("Apple", "7 plus", 2),'
           f'("Samsung", "S20", 3),'
           f'("Xiaomi", "Redmi Note 12 Pro", 4)')
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
