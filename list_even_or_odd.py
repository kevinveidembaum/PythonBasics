def main():
    valores = list()
    pares = list()
    impares = list()
    while True:
        valores.append(int(input("Digite um valor: ")))
        escolha = str(input("Quer continuar? [S/N] "))
        if escolha in 'Nn':
            print("-=" * 15)
            for i in valores:
                if i % 2 == 0:
                    pares.append(i)
                else:
                    impares.append(i)
            print(f"Lista completa: {valores}")
            print(f"Lista dos pares: {pares}")
            print(f"Lista dos impares: {impares}")
            break

if __name__ == "__main__":
    main()