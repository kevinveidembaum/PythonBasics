from random import randint
from time import sleep
def main():
    jogo()

def jogo():
    jogadas = ('Pedra', 'Papel', 'Tesoura')
    jogador = int(input("""Suas opções:
[0]Pedra
[1]Papel
[2]Tesoura
"""))
    print("JO")
    sleep(0.75)
    print("KEN")
    sleep(0.75)
    print("POO!!")
    sleep(0.75)
    computador = randint(0, 2)
    print("-=" * 14)
    print(f"Você escolheu {jogadas[jogador]}.\nComputador escolheu {jogadas[computador]}.")
    print("-=" * 14)
    if computador == 0: #computador jogou pedra
        if jogador == 0:
            print("EMPATE")
        elif jogador == 1:
            print("JOGADOR GANHOU")
        elif jogador == 2:
            print("JOGADOR PERDEU")
    elif computador == 1: #computador jogou papel
        if jogador == 0:
            print("JOGADOR PERDEU")
        elif jogador == 1:
            print("EMPATE")
        elif jogador == 2:
            print("JOGADOR GANHOU")
    elif computador == 2: #computador jogou tesoura
        if jogador == 0:
            print("JOGADOR GANHOU")
        elif jogador == 1:
            print("JOGADOR PERDEU")
        elif jogador == 2:
            print("EMPATE")

if __name__ == "__main__":
    main()