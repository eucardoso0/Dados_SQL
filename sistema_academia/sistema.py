import pandas as pd 
import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "sistema_academia"
)

tabelas =['Alunos','Planos','Matriculas','Pagamentos','Presencas','Instrutores']

for tabela in tabelas:

 arq = pd.read_sql(f"SELECT * FROM {tabela}", conexao)
 arq.to_csv(f"{tabela}.csv", index= False)

 ##### Agrupei 3 tabelas para facilitar um pouco e os valos nulos serão tirados no Power BI

 query = """ 
SELECT 
    a.id_aluno,
    a.nome AS nome_aluno,
    a.email,
    a.telefone,
    a.sexo,
    a.data_nascimento,
    
    m.id_matricula,
    m.data_inicio,
    m.data_fim,
    
    p.nome AS nome_plano,
    p.preco_mensal,
    p.duracao_meses,
    
    pag.data_pagamento,
    pag.valor_pago,
    pag.forma_pagamento,
    
    pr.data_presenca,
    pr.hora_entrada

FROM alunos a
LEFT JOIN matriculas m ON a.id_aluno = m.id_aluno
LEFT JOIN planos p ON m.id_plano = p.id_plano
LEFT JOIN pagamentos pag ON m.id_matricula = pag.id_matricula
LEFT JOIN presencas pr ON a.id_aluno = pr.id_aluno

"""

df = pd.read_sql(query, conexao)
df.to_csv('dados_academia_completo_1.csv', index=False)





