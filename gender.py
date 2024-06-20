def main():
    genero = str(input("Digite seu sexo: [M][F]")).strip()[0]
    while genero not in 'MmFf':
        genero = str(input("Dados invalidos. Por favor informe seu sexo: ")).strip()[0]
    

    if genero in 'Ff':
        print("Obrigado, sexo Feminino confirmado com sucesso!")
    else:
        print("Obrigado, sexo Masculino confirmado com sucesso!")

if __name__ == "__main__":
    main()
