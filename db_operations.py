import sqlite3

# 1° vez = cria um db
# nas proximas ele so faz a conexao
connection=sqlite3.connect('chest.db')
# cursor é para executar funções SQL
cursor = connection.cursor()