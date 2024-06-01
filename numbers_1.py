def main ():
    analise_numero()

def analise_numero():
    n = int(input("Digite um número: "))
    uni = n // 1 % 10
    dez = n // 10 % 10
    cen = n // 100 % 10
    mil = n // 1000 % 10
    print("Analisando número...")
    print(f"Unidades: {uni}")
    print(f"Dezenas: {dez}")
    print(f"Centenas: {cen}")
    print(f"Milhares: {mil}")

if __name__ == "__main__":
    main()
