distancia_viagem = float(input("Qual é a distância da sua viagem em Km? "))
distancia_minima = 1
distancia_minima_desconto = 200
frase = "E o preço da sua passagem será de R${:.2f}."

if distancia_viagem < distancia_minima:
    print("Oops! Valor inválido!")

else:
    print("Você está prestes a começar uma viagem de {}Km.".format(distancia_viagem))
    if distancia_viagem <= distancia_minima_desconto:
        preco_viagem = distancia_viagem * 0.50
        print(frase.format(preco_viagem))
    else:
        preco_viagem = distancia_viagem * 0.45
        print(frase.format(preco_viagem))

# 0.50 por Km até 200Km
# 0.45 por Km para mais de 200Km
