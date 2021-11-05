def aluno_notas(* notas, situacao=False):
    """
    :param notas: uma ou mais notas do aluno.
    :param situacao: valor opcional, indica a situação do aluno.
    :return: dicionário com dados do aluno(total, maximo, minimo, media, situação)
    """
    resultado = dict()
    resultado["Total"] = len(notas)
    resultado["Maior"] = max(notas)
    resultado["Menor"] = min(notas)
    resultado["Média"] = sum(notas) / len(notas)
    if situacao:
        if resultado["Média"] >= 8:
            resultado["Situação"] = 'BOA'
        elif 6 <= resultado["Média"] < 8:
            resultado["Situação"] = 'RAZOÁVEL'
        else:
            resultado["Situação"] = 'RUIM'

    return resultado


resposta = aluno_notas(4, 4, 5, situacao=True)
print(resposta)
