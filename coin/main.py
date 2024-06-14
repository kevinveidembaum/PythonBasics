import moeda

def main():
    user = float(input("Digite um valor monetário: R$"))
    print(f"O dobro de {moeda.formatacao(user)} é {moeda.formatacao(moeda.dobro(user))}")
    print(f"A metade de {moeda.formatacao(user)} é {moeda.formatacao(moeda.metade(user))}")
    print(f"O valor de {moeda.formatacao(user)} reajustado para 10% a mais, é {moeda.formatacao(moeda.reajuste(user, 10))}")
    print(f"O valor de {moeda.formatacao(user)} reajustado para 23% a menos, é {moeda.formatacao(moeda.reajuste(user, 23, False))}")

if __name__ == "__main__":
    main()