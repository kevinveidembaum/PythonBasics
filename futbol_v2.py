def main():
    jogador = dict()
    pontos = list()
    time = list()
    while True:
        jogador['nome'] = str(input("Digite o nome do jogador: "))
        partidas = int(input(f"Informe quantas partidas {jogador['nome']} jogou: "))
        pontos.clear()
        #loop para gols na partida
        for i in range(0, partidas):
            pontos.append(int(input(f"Quantos gols na partida {i+1}? ")))
        
        jogador['gols'] = pontos[:]
        jogador['total'] = sum(pontos)
        time.append(jogador.copy())
        escolha = str(input("Quer continuar? [S/N]"))
        if escolha not in 'NnSs':   #verificação resposta usuario
            while escolha not in 'NnSs':
                print("ERRO. Por favor informe [S/N]")
                escolha = str(input("Quer continuar? [S/N]"))
        if escolha in 'Nn': #encerra programa
            print("<<< ENCERRADO >>>")
            break


    print("-=" * 40)
    print("cod", end=' ')
    for i in jogador.keys():
        print(f"{i:<15}", end='')
    print()

    for k, v in enumerate(time):
        print(f"{k:<4} ", end='')
        for d in v.values():
            print(f"{str(d):<15}", end='')
        print()
    print("-=" * 40)



    

if __name__ == "__main__":
    main()