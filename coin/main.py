from utilities import monetary, data

def main():
    user = data.inputDinheiro("Digite um valor monetário: ")
    print(f"O dobro de {monetary.formatacao(user)} é {monetary.dobro(user, True)}")
    print(f"A metade de {monetary.formatacao(user)} é {monetary.metade(user, True)}")
    print(f"O valor de {monetary.formatacao(user)} reajustado para 10% a mais, é {monetary.reajuste(user, 10, True)}")
    print(f"O valor de {monetary.formatacao(user)} reajustado para 23% a menos, é {monetary.reajuste(user, 23, False)}")

if __name__ == "__main__":
    main()