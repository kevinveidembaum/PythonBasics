def main():
    print("Calculando ÁREA")
    comprimento = float(input("Digite o comprimento: "))
    largura = float(input("Digite a largura: "))
    print(f"O valor da área será de: {area(comprimento, largura)}m²")


def area(comp, larg):
    return comp * larg



if __name__ == "__main__":
    main()