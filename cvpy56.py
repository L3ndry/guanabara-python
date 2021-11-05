idades = 0
maior_idade = 0
mais_velho_nome = ""
quantidade_mulheres = 0

for cada_pessoa in range(1, 5):

    print(f"- - - {cada_pessoa}ª PESSOA - - -")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").upper()

    idades += idade

    if cada_pessoa == 1:
        maior_idade = idade
        mais_velho_nome = nome

    elif idade > maior_idade and sexo == "M":
        maior_idade = idade
        mais_velho_nome = nome

    elif sexo == "F" and idade < 20:
        quantidade_mulheres += 1

media_idades = idades / 4

print(f"A média de idade do grupo é de {media_idades:.1f} anos.")
print(f"O homem mais velho tem {maior_idade} anos e se chama {mais_velho_nome}.")
print(f"Ao todo são {quantidade_mulheres} mulheres com menos de 20 anos.")
