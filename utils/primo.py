def primos(num1: float):
    try:
        divisao = 0
        contador = 0
        numeros = 1
        if (num1 > 0):
            while (contador < 9):
                if ((num1 % numeros) == 0):
                    divisao += 1
                contador +=1
                numeros +=1
            if (divisao < 2):
                return(True)
            else:
                return(False)
        else:
            return("Erro (E03):  valor não suportado! \nFavor digitar um valor válido! \n")
    except ValueError:
        erro01 = ("Erro (E01):  valor não suportado! \nFavor digitar um valor válido! \n\n\nPossiveis Soluções: \nDigitar um número racional \nCaso o valor possua virgula substituir a ',' por '.' \n")
        return (erro01)
    except TypeError:
        erro02 = ("Erro (E02):  valor não suportado! \nFavor digitar um valor válido! \n")
        return(erro02)
print(primos(-24))