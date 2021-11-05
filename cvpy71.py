print("      BANCO CEV\n", "=" * 20)

valor = int(input("Qual valor você quer sacar? R$"))
quantidade_cinquenta = quantidade_vinte = quantidade_dez = quantidade_um = 0
print("=" * 20)

while valor >= 50:
    valor -= 50
    quantidade_cinquenta += 1
while valor >= 20:
    valor -= 20
    quantidade_vinte += 1
while valor >= 10:
    valor -= 10
    quantidade_dez += 1

quantidade_um = valor

if quantidade_cinquenta > 0:
    print(f"Total de {quantidade_cinquenta} cédulas de R$50.")
if quantidade_vinte > 0:
    print(f"Total de {quantidade_vinte} cédulas de R$20.")
if quantidade_dez > 0:
    print(f"Total de {quantidade_dez} cédulas de R$10.")
if quantidade_um > 0:
    print(f"Total de {quantidade_um} cédulas de R$1.")

print("=" * 20,"\nVolte sempre ao BANCO CEV! Tenha um bom dia!")
