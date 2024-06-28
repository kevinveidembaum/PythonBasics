def main():
    while True:
        try:
            inteiro = int(input("Digite um número Inteiro: "))
            break
        except ValueError:
            print(f"ERRO: Por favor informe um número Inteiro Válido.")

    while True:
        try:
            real = float(input("Digite um número Real: "))
            break
        except ValueError:
            print(f"ERRO: Por favor informe um número Real Válido.")
        
    print(f"O número Inteiro digitado foi {inteiro} e o Real {real}")

if __name__ == "__main__":
    main()