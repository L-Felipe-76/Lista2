def verificador (num0: float):
    try:    
        num1 = num0
        resposta = str('')
    
        if (num1 > 0):
            resposta = 'P'
            return(resposta)
        elif (num1 <= 0):
            resposta = 'N'
            return(resposta)
    except ValueError:
        erro01 = ("Erro (E01):  valor não suportado! \nFavor digitar um valor válido! \n\n\nPossiveis Soluções: \nDigitar um número racional \nCaso o valor possua virgula substituir a ',' por '.' \n")
        return (erro01)
    except TypeError:
        erro02 = ("Erro (E02):  valor não suportado! \nFavor digitar um valor válido! \n")
        return(erro02)