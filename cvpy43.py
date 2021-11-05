peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = peso / (altura ** 2)

print(f"O seu Imc é igual a {imc:.2f}.")
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está no peso ideal.")
elif 25 <= imc < 30:
    print("Você está sobrepeso.")
elif 30 <= imc < 40:
    print("Você está obeso.")
else:
    print("Você está en obesidade mórbida.")
