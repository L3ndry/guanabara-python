aluno = dict()
aluno["Nome"] = str(input("Nome: ")).title().strip()
aluno["Média"] = float(input(f"Média de {aluno['Nome']}: "))

print("- " * 10)
if aluno['Média'] >= 7:
    aluno['Situação'] = "Aprovado."
elif 5 < aluno['Média'] < 7:
    aluno['Situação'] = "Recuperação."
else:
    aluno['Situação'] = "Reprovado."

for chave, valor in aluno.items():
    print(f" - {chave} é igual a {valor}")
