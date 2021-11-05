from datetime import date

maior_idade = 0
menor_idade = 0
ano_atual = date.today().year

for cada_pessoa in range(0, 7):
    ano_nascimento = int(input("Em que ano a pessoa nasceu? "))
    idade = ano_atual - ano_nascimento
    maior = 18
    if idade >= maior:
        maior_idade += 1
    else:
        menor_idade += 1

print(f"Ao todo tivemos {maior_idade} pessoa(s) maior(es) de idade.")
print(f"E também tivemos {menor_idade} pessoa(s) menor(es) de idade")
