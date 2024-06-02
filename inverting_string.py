def main():
    frase = str(input("Escreva uma frase: ")).strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = ''
    for letra in range(len(junto) - 1, -1, -1):
        inverso += junto[letra]
    print(junto, inverso)
    if junto == inverso:
        print("Temos um caso de palíndromo")
    else:
        print("Não configura um caso de palíndromo")

if __name__ == "__main__":
    main()