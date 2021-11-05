from datetime import datetime

usuario = dict()
usuario['Nome'] = str(input("Nome: ")).title().strip()
usuario['Idade'] = datetime.now().year - int(input("Ano de nasimento: "))
usuario['Ctps'] = int(input("Carteira de trabalho (0 não tem): "))

if usuario['Ctps'] > 0:
    usuario['Contratação'] = int(input("Ano de contratação: "))
    usuario['Salário'] = float(input("Salário: R$"))

print("- " * 15)
for chave, valor in usuario.items():
    print(f" - {chave} tem o valor {valor}.")
