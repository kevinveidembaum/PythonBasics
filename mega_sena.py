from random import randint
from time import sleep

def main():
    valores =  list()
    jogos = list()
    c = 0

    print('='*30)
    print("   PALPITES PARA MEGA SENA   ")
    print('='*30)

    qntd_jogos = int(input("Quantos jogos quer realizar? "))
    while c < qntd_jogos:
        qntd_num = 0
        while True:
            num = randint(0, 60)
            if num not in valores:
                valores.append(num)
                qntd_num += 1
            if qntd_num >= 6:
                break
        c += 1
        valores.sort()
        jogos.append(valores[:])
        valores.clear()
    print("Processando...")
    for indice, jogo in enumerate(jogos):
        print(f"{indice+1}° jogo: {jogo}")
        sleep(0.75)

if __name__ == "__main__":
    main()
