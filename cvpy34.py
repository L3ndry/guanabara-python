salario_funcionario = float(input("Qual é o salário do funcionário? R$"))

if salario_funcionario > 1250:
    aumento = salario_funcionario + (salario_funcionario * 0.1)
else:
    aumento = salario_funcionario + (salario_funcionario * 0.15)

print(f"Quem ganhava R${salario_funcionario:.2f} passa a ganhar R${aumento:.2f} agora.")

# superior a 1.250.00, 10%
# inferiores ou iguais, 15%
