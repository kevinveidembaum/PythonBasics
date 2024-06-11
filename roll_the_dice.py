from random import randint
from time import sleep
from operator import itemgetter
def main():
    ranking = dict()
    jogadas = {
        'jogador1': randint(1, 10),
        'jogador2': randint(1, 10),
        'jogador3': randint(1, 10),
        'jogador4': randint(1, 10),
        'jogador5': randint(1, 10)
    }
    print('-=' *30)
    for k, v in jogadas.items():
        print(f"O {k} sorteou {v} no dado.")
        sleep(1)
    print('-=' *30)

    ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
    print(f"{'RANKING FINAL':^50}")
    print('-=' *30)
    for pos, valor in enumerate(ranking):
        print(f"{pos+1}° posição: {valor[0]} com {valor[1]}")
        sleep(1)
    print('-=' *30)




if __name__ == "__main__":
    main()