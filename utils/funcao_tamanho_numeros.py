import math

def tamanho_numeros ():
    try:
        num1 = float(input('Digite o valor a ser medido: '))
        str_num1 = str(num1).split('.', 1)
        limitador = len(str_num1[1])

        parte_decimal, parte_inteira = math.modf(num1)
        parte_decimal_limitada = round(parte_decimal, limitador)
        str_parte_decimal = str(parte_decimal_limitada)
        str_parte_inteira = str(parte_inteira)
        
        if (num1 < 0):
            quantidade_digitos_int = int(len(str_parte_inteira) - 3)
            quantidade_digitos_dec = int(len(str_parte_decimal) - 3)
        elif (num1 > 0):
            quantidade_digitos_int = int(len(str_parte_inteira) - 2)
            quantidade_digitos_dec = int(len(str_parte_decimal) - 2)

        if (parte_decimal != 0):
            return(f"O número possui {quantidade_digitos_int} digitos inteiros e {quantidade_digitos_dec} digitos decimais! \nTendo {quantidade_digitos_int + quantidade_digitos_dec} digitos no total.")
        else:
            return(f"O número possui {quantidade_digitos_int} digitos")
        
    except ValueError:
        erro01 = ("Erro (E01):  valor não suportado! \nFavor digitar um valor válido! \n\n\nPossiveis Soluções: \nDigitar um número racional \nCaso o valor possua virgula substituir a ',' por '.' \n")
        return (erro01)
    except TypeError:
        erro02 = ("Erro (E02):  valor não suportado! \nFavor digitar um valor válido! \n")
        return(erro02)