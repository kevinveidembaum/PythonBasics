def main():
    jogador = dict()
    pontos = list()
    jogador['nome'] = str(input("Digite o nome do jogador: "))
    partidas = int(input(f"Informe quantas partidas {jogador['nome']} jogou: "))
    
    for i in range(0, partidas):
        pontos.append(int(input(f"Quantos gols na partida {i+1}? ")))
        
    jogador['gols'] = pontos[:]
    jogador['total'] = sum(pontos)

    print("-=" * 30)
    print(jogador)
    print("-=" * 30)

    for k, v in jogador.items():
        print(f"No campo {k} tem {v}")

    print("-=" * 30)

    print(f"O jogador {jogador['nome']} fez: ")
    for i, v in enumerate(jogador['gols']):
        print(f"Na partida {i+1} fez {v} gols")

if __name__ == "__main__":
    main()