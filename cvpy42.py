segmento1 = float(input("Primeiro segmento: "))
segmento2 = float(input("Segundo segmento: "))
segmento3 = float(input("Terceiro segmento: "))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    if segmento1 == segmento2 == segmento3:
        print("Esses segmentos podem formar um triângulo EQUILÁTERO.")
    elif segmento1 == segmento2 or segmento1 == segmento3 or segmento2 == segmento3:
        print("Esses segmentos podem formar um triângulo ISÓSCELES.")
    else:
        print("Esses segmentos podem formar um triângulo ESCALENO.")

else:
    print("Esses segmentos NÃO PODEM formar um triângulo.")
