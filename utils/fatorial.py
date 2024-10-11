def fatorial(num1: int):
    try:
        CONTADOR = int(0)
        limitador = num1
        fatorial = num1
        while (CONTADOR < limitador - 1):
            fatorial = fatorial * (num1 - 1)
            num1 -= 1
            CONTADOR += 1
        return fatorial
    except ValueError:
        erro01 = ("Erro (E01):  valor não suportado! \nFavor digitar um valor válido! \n\n\nPossiveis Soluções: \nDigitar um número racional \nCaso o valor possua virgula substituir a ',' por '.' \n")
        return (erro01)
    except TypeError:
        erro02 = ("Erro (E02):  valor não suportado! \nFavor digitar um valor válido! \n")
        return(erro02)