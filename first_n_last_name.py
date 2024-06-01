def main():
    name()

def name():
    nome = str(input("Informe seu nome completo: ")).strip().lower().title().split()
    print(f"Seu primeiro nome é {nome[0]}")
    print(f"E seu último nome é {nome[len(nome) - 1]}")

if __name__ == "__main__":
    main()