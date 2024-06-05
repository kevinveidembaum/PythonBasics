def main():
    numeros = list()
    while True:
        num = int(input("Digite um valor: "))
        if num not in numeros:
            numeros.append(num)
            print("Número adicionado...")
        elif num in numeros:
            print("Número duplicado, digite outro valor.")
        
        escolha = str(input("Quer continuar? [S/N] ")).strip()
        if escolha in 'Nn':
            print("Programa encerrado com Sucesso!")
            print(f"Os valores digitados foram: {sorted(numeros)}")
            break

if __name__ == "__main__":
    main()