def main():
    silva()

def silva():
    nome = str(input("Digite seu nome completo: ")).strip()
    print(f"Possui Silva no nome: {'silva' in nome.lower()}")    

if __name__ == "__main__":
    main()