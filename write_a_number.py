def main():
    extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dessesete', 'dezoito', 'dezenove', 'vinte')

    while True:
        n = int(input("Digite um número entre 0 e 20: (999 para encerrar) "))
        if n == 999:
            print("Programa encerrado com sucesso!")
            break
        while n > 20 or n < 0:
            n = int(input("Número Inválido. Digite um número entre 0 e 20: (999 para encerrar) "))

        print(extenso[n])


if __name__ == "__main__":
    main()