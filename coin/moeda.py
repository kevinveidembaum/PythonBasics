def reajuste(preco, taxa, aumentar=True):
    """ 
    return the value of money with a tax

    Args:
        preco (float): money value
        taxa (int): the percentage
        aumentar (bool): decides if its a increase or decrease
    """

    if aumentar:
        res = preco + (preco * taxa/100)
        return res
    else:
        res = preco - (preco * taxa/100)
        return res


def dobro(preco):
    """
    return the double part of a number
    """

    res = preco * 2
    return res


def metade(preco):
    """ 
    return the half of a number
    """

    res = preco/2
    return res


def formatacao(moeda):
    """
    return the formatted number
    """

    return f'R${moeda:.2f}'.replace('.', ',')