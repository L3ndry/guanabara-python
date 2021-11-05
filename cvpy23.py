numero = float(input("Informe um número: "))
numero2 = int(numero)
unidade = numero2 // 1 % 10
dezena = numero2 // 10 % 10
centena = numero2 // 100 % 10
milhar = numero2 // 1000 % 10
print(f"Analisando o número {numero2}\nUnidade: {unidade}")
print(f"Dezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}")
