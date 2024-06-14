def reajuste(preco, taxa, aumentar=False, format=True):
    """ 
    return the value of money with a tax

    Args:
        preco (float): money value
        taxa (int): the percentage
        aumentar (bool): decides if its a increase or decrease
        format (bool): give the formatted number
    """

    if aumentar:
        res = preco + (preco * taxa/100)
        return res
    else:
        res = preco - (preco * taxa/100)
        return res if format is False else formatacao(res)


def dobro(preco, format=False):
    """
    return the double part of a number

    format (bool): give the formatted number
    """

    res = preco * 2
    return res if format is False else formatacao(res)


def metade(preco, format=False):
    """ 
    return the half of a number

    format (bool): give the formatted number
    """

    res = preco/2
    return res if format is False else formatacao(res)


def formatacao(moeda):
    """
    return the formatted number
    """

    return f'R${moeda:.2f}'.replace('.', ',')