def verif_vogais(str1: str):
    try:
        lista_letras = list(str1)
        limitador = len(str1)
        CONTADOR = int(0)
        vogais = int(0)
        teste = str('aeiouAEIOU')
        while (CONTADOR < limitador):
            if lista_letras[CONTADOR] in teste:
                vogais += 1
            CONTADOR += 1
        return (vogais)
    except ValueError:
        erro01 = ("Erro (E01):  valor não suportado! \nFavor digitar um valor válido! \n\n\nPossiveis Soluções: \nDigitar um número racional \nCaso o valor possua virgula substituir a ',' por '.' \n")
        return (erro01)
    except TypeError:
        erro02 = ("Erro (E02):  valor não suportado! \nFavor digitar um valor válido! \n")
        return(erro02)
