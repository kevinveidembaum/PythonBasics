import moeda

def main():
    user = float(input("Digite um valor monetário: R$"))
    print(f"O dobro de R${user} é R${moeda.dobro(user)}")
    print(f"A metade de R${user} é R${moeda.metade(user)}")
    print(f"O valor de R${user} reajustado para 10% a mais, é R${moeda.reajuste(user, 10)}")
    print(f"O valor de R${user} reajustado para 23% a menos, é R${moeda.reajuste(user, 23, False)}")

if __name__ == "__main__":
    main()