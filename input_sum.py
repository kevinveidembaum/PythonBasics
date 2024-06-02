def main():
    soma = 0
    for x in range(0, 6):
        num = int(input(f"Digite o {x+1}º número: "))
        if num%2 == 0:
            soma += num
    print(f"O resultado do somatório de todos os números pares é {soma}")

if __name__ == "__main__":
    main()