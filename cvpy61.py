print("Gerador de PA")
print("-" * 15)

primeiro_termo = int(input("Primeiro termo: "))
razao_pa = int(input("Razão da PA: "))
soma = primeiro_termo

contador = 10
while contador > 0:
    print(f"{soma} -> ", end="")
    soma += razao_pa
    contador -= 1
    if contador == 0:
        print("FIM")