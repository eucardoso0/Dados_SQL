import mysql.connector


criar_conexao = host_name = "localhost"
user_name = "root"
user_password = ""
db_name = "pythonsql"

conexao = mysql.connect(criar_conexao)
print("conexão Bem Sucedida")