def main():
    pessoas = list()
    sujeito = dict()
    soma = media = 0
    while True:
        sujeito['nome'] = str(input("Insira o nome da pessoa: "))
        sujeito['sexo'] = str(input("Informe Sexo: [F/M]")).strip()

        if sujeito["sexo"] not in 'FfMm':
            while sujeito["sexo"] not in 'FfMm':
                print("ERRO. Por favor insira [F/M]")
                sujeito['sexo'] = str(input("Informe Sexo: [F/M]")).strip()

        sujeito['idade'] = int(input("Informe a idade: "))
        soma += sujeito["idade"]
        pessoas.append(sujeito.copy())
        escolha = str(input("Quer continuar? [S/N]")).strip()
        
        if escolha not in 'SsNn':
            while escolha not in 'SsNn':
                print("ERRO. Por favor insira [S/N]")
                escolha = str(input("Quer continuar? [S/N]"))
        if escolha in 'Nn':
            print("Programa Encerrado")
            print('-=' *30)
            break

    #trabalhando com os valores da lista
    media = soma / len(pessoas)

    #printando os valores desejados
    print(f"Ao todo temos {len(pessoas)} pessoas")
    print(f"A média de idade das pessoas é {int(media)} anos")
    print(f"As mulheres cadastradas foram ", end='')
    for p in pessoas:
        if p['sexo'] in 'Ff':
            print(f"{p['nome']}, ", end='')
    print()
    print(f"As pessoas com idade acima da média foram: ")
    for p in pessoas:
        if p['idade'] > media:
            print(f"{p['nome']}, ", end='')
    print()
    
if __name__ == "__main__":
    main()