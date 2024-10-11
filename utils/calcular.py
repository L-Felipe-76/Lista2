from calculadora import *

def calcular(num1: float, num2: float, operacao: str):
    try:
        ESCOLHA_USUARIO = 0
        while (ESCOLHA_USUARIO != 1):
            if (operacao == '+'):
                resultado = somar(num1, num2)
                ESCOLHA_USUARIO = 1
                return (resultado)
            elif (operacao == '-'):
                resultado = subtrair(num1, num2)
                ESCOLHA_USUARIO = 1
                return (resultado)
            elif (operacao == '/'):
                resultado = dividir(num1, num2)
                ESCOLHA_USUARIO = 1
                return (resultado)
            elif (operacao == '*'):
                resultado = multiplicar(num1, num2)
                ESCOLHA_USUARIO = 1
                return (resultado)
                
    except ValueError:
        erro01 = ("Erro (E01):  valor não suportado! \nFavor digitar um valor válido! \n\n\nPossiveis Soluções: \nDigitar um número racional \nCaso o valor possua virgula substituir a ',' por '.' \n")
        return (erro01)
    except TypeError:
        erro02 = ("Erro (E02):  valor não suportado! \nFavor digitar um valor válido! \n")
        return(erro02)