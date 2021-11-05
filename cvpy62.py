print("Gerador de PA")
print("-" * 15)

primeiro_termo = int(input("Primeiro termo: "))
razao_pa = int(input("Razão da PA: "))
soma = primeiro_termo

contador = 10
quantidade_termos = contador
while contador > 0:
    print(f"{soma} -> ", end="")
    soma += razao_pa
    contador -= 1
    if contador == 0:
        print("PAUSA")
        continuar = False
        while not continuar:
            quantidade = int(input("Quantos termos você quer mostrar a mais? "))
            if quantidade == 0:
                print(f"Progressão finalizada com {quantidade_termos} termos mostrados.")
                continuar = True
                break
            else:
                quantidade_termos += quantidade
                contador += quantidade
                continuar = True
