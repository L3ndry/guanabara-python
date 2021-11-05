velocidade = float(input("Qual é a velocidade atual do carro? "))
limite_permitido = 80
if velocidade > limite_permitido:
    multa = (velocidade - 80) * 7
    print(f"MULTADO! Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de R${multa:.2f}!")
print("Tenha um bom dia! Dirija com segurança!")
