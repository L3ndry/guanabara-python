from datetime import date
ano_nascimento = int(input("Qual ano você nasceu? "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f"Quem nasceu em {ano_nascimento} em {ano_atual} tem {idade} anos.")
idade_alistamento = 18
if idade < idade_alistamento:
    ano_alistamento = (18 - idade) + ano_atual
    print(f"Seu alistamento será em {ano_alistamento}")

elif idade > idade_alistamento:
    ano_alistamento = idade - 18
    print(f"Você já deveria ter se alistado há {ano_alistamento} ano(s).")
    print(f"Seu alistamento foi em {ano_atual - ano_alistamento}")

else:
    print("Você deve se alistar IMEDIATAMENTE!")
