import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('plantao.db')

# Adicionar um novo registro
conn.execute("INSERT INTO plantao (plantonista, data) VALUES ('Berbert', '2023-03-30')")

# Salvar as mudanças
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
