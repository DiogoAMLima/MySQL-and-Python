import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='*****',
    database='animes',
)

cursor = conexao.cursor()

# comando = (f'CREATE TABLE personagens(id int PRIMARY KEY AUTO_INCREMENT NOT NULL, nome VARCHAR(50), idade INT, '
            # f'main TINYINT)')
# comando = (f'INSERT INTO personagens(nome, idade, main)'
#            f'VALUES'
#            f'("Uzumaki Naruto", 32, 1),'
#            f'("Uchiha Sasuke", 32, 0),'
#            f'("Yusuke Urameshi", 18, 1),'
#            f'("Hiei", 20, 0),'
#            f'("Vegeta", 48, 0),'
#            f'("Sanji", 21, 0),'
#            f'("Luffy", 19, 1)')
# comando = f'UPDATE personagens SET nome = "Monkey D Luffy" WHERE id = 7'
# comando = f'UPDATE personagens SET nome = "Vinsmoke Sanji" WHERE id = 6'
# comando = f'SELECT * FROM personagens ORDER BY idade ASC'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(f'{resultado}')

# comando = f'SELECT SUM(idade) AS "Soma das idades" FROM personagens'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(f'{resultado}')

# comando = f'SELECT AVG(idade) AS "Médias das idades" FROM personagens'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(f'{resultado}')

# comando = f'SELECT SUM(idade) AS "Médias das idades dos principais" FROM personagens WHERE main = 1'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(f'{resultado}')

# comando = f'SELECT nome, COUNT(*) AS "Qntd de personagens" FROM personagens GROUP BY nome'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(f'{resultado}')

# comando = f'SELECT COUNT(nome) FROM personagens'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(f'{resultado}')

conexao.commit()

cursor.close()
conexao.close()
