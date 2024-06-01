def main ():
    sentence()

def sentence():
    frase = str(input("Escreva uma frase: ")).strip().lower()
    print(f"Nessa frase aparece a letra A, {frase.count('a')}, vezes.")
    print(f"A primeira letra A aparece na posição {frase.find('a') + 1}")
    print(f"A última letra A aparece na posição {frase.rfind('a') + 1}")

if __name__ == "__main__":
    main()