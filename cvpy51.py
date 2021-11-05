print("10 TERMOS DE UMA P.A\n")
primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro_termo

for cada_termo in range(1, 11):
    print(f"{termo} >", end=" ")
    termo += razao

print("ACABOU")
