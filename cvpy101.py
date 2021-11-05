def idade(ano_nascimento):
    from datetime import datetime
    atual = datetime.now().year - ano_nascimento
    return atual


resposta = int(input("Em que ano você nasceu? "))
idade_atual = idade(resposta)
print(f"Com {idade_atual} anos:", end=" ")
if idade_atual < 16:
    print("NÃO VOTA.")
elif 16 <= idade_atual <= 17:
    print("VOTO OPCIONAL.")
else:
    print("VOTO OBRIGATÓRIO.")
