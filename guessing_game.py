from random import randint
from time import sleep

def main():
    computador = randint(1, 5)
    print("-=-" * 20)
    print("Estou pensando em um número entre 1 até 5. Adivinhe qual é.")
    print("-=-" * 20)
    jogador = int(input())
    print("Processando...")
    sleep(2)
    if(jogador == computador):
        print(f"ACERTOU. Eu estava pensando no número {computador} mesmo")
    else:
        print(f"ERROU. Eu pensei no {computador} e não no {jogador}")


if __name__ == "__main__":
    main()