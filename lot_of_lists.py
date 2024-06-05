def main():
    pessoas = list()
    dados = list()
    maior_peso = menor_peso = 0
    while True:
        dados.append(str(input("Digite um nome: ")))
        dados.append(float(input("Digite a peso: ")))
        if len(pessoas) == 0:
            maior_peso = menor_peso = dados[1]
        else:
            if dados[1] > maior_peso:
                maior_peso = dados[1]
            if dados[1] < menor_peso:
                menor_peso = dados[1]
        pessoas.append(dados[:])
        dados.clear()
        escolha = str(input("Quer continuar? [S/N] "))
        if escolha in 'Nn':
            break
    
    print("-=" * 30)
    print(f"Foram cadastradas {len(pessoas)} pessoas.")
    print(f"O maior peso cadastrado foi de {maior_peso}Kg. Peso de ", end='')
    for p in pessoas:
        if p[1] == maior_peso:
            print(f"{p[0]} ", end='')
    print(f"\nO menor peso cadastrado foi de {menor_peso}Kg. Peso de ", end='')
    for p in pessoas:
        if p[1] == menor_peso:
            print(f"{p[0]} ", end='')

if __name__ == "__main__":
    main()