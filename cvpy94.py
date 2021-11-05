usuario = dict()
cadastros = list()
idades = list()

rodando = True
while rodando:
    usuario['Nome'] = str(input("Nome: ")).strip().title()
    while True:
        sexo = str(input("Sexo: [M/F] ")).strip().upper()
        if sexo != "M" and sexo != "F":
            print("Oops! Valor inválido! Digite novamente.")
        else:
            usuario['Sexo'] = sexo
            break
    usuario['Idade'] = int(input("Idade: "))

    idades.append(usuario['Idade'])
    cadastros.append(usuario.copy())
    usuario.clear()

    while True:
        resposta = str(input("Quer continuar? [S/N] ")).strip().upper()
        if resposta == "S":
            break
        elif resposta == "N":
            rodando = False
            break
        else:
            print("Oops! Valor inválido! Digite novamente.")

print("- " * 20)

print(f"Ao todo temos {len(cadastros)} pessoas cadastradas.")
media = sum(idades) / len(cadastros)
print(f"A média de idade é de {media:.2f} anos.")
print(f"As mulheres cadastradas foram:", end=" ")
for pessoa in cadastros:
    if pessoa['Sexo'] == "F":
        print(pessoa['Nome'], end=" ")
print(f"\nLista das pessoas que estão acima da média:")
for pessoa in cadastros:
    if pessoa['Idade'] > media:
        print(pessoa)
