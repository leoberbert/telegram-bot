import sqlite3

# Estabelecendo conexão com o banco de dados
conn = sqlite3.connect('plantao.db')

# Criando um cursor para executar comandos SQL
cursor = conn.cursor()

# Executando uma consulta SELECT em uma tabela
cursor.execute("SELECT * FROM plantao")

# Obtendo todos os resultados da consulta
resultados = cursor.fetchall()

# Imprimindo os resultados na tela
for linha in resultados:
    print(linha)

# Fechando a conexão com o banco de dados
conn.close()
