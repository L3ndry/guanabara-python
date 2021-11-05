valor_casa = float(input("Digite o valor da casa: R$"))
salario_comprador = float(input("Digite o salário do comprador: R$"))
anos_financiamento = int(input("Digite quantos anos de financiamento: "))
prestacao = valor_casa / (anos_financiamento * 12)
minimo_mensal = salario_comprador * 0.3
print(f"""Para pagar uma casa de R${valor_casa:.2f} em {anos_financiamento} anos a
prestação será de R${prestacao:.2f}.""")
if prestacao <= minimo_mensal:
    print("Empréstimo ACEITO!")
else:
    print("Empréstimo NEGADO!")
