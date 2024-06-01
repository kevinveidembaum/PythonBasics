def main():
    stringMethods()

def stringMethods():
    nome = str(input("Digite seu nome: ")).strip()
    primeiro_nome = nome.split()
    print(f"Seu nome em maiúsculas {nome.upper()}")
    print(f"Seu nome em minúsculas {nome.lower()}")
    print(f"Seu nome tem {len(nome) - nome.count(" ")} letras")
    print(f"Seu primeiro nome é {primeiro_nome[0]} e ele tem {len(primeiro_nome[0])} letras")

if __name__ == "__main__":
    main()