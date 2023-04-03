import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('plantao.db')

# Criar uma tabela chamada plantao
conn.execute('''
    CREATE TABLE plantao (
        plantonista TEXT,
        data TEXT
    );
''')

# Fechar a conexão com o banco de dados
conn.close()