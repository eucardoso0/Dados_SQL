import pandas as pd

# === 1. Carregar os arquivos CSV ===
alunos = pd.read_csv("Alunos.csv")
matriculas = pd.read_csv("Matriculas.csv")
planos = pd.read_csv("Planos.csv")
pagamentos = pd.read_csv("Pagamentos.csv")
presencas = pd.read_csv("Presencas.csv")

# === 2. Unir os dados ===

# alunos + matriculas
df = pd.merge(alunos, matriculas, on="id_aluno", how="left")

# + planos
df = pd.merge(df, planos, on="id_plano", how="left")

# + pagamentos
df = pd.merge(df, pagamentos, on="id_matricula", how="left")

# + presencas
df = pd.merge(df, presencas, on="id_aluno", how="left")

# === 3. Salvar como CSV unificado ===
df.to_csv("academia_dados_completos.csv", index=False)

print("✅ Arquivo 'academia_dados_completos.csv' gerado com sucesso!")
