from random import randint
def main():
    print("-="*13)
    print("VAMOS JOGAR ÍMPAR OU PAR")
    print("-="*13)
    game()

def exibir_resultado(ganhou, computador, jogador, resultado):
    res_msg = "VENCEU" if ganhou == True else "PERDEU"
    print(f"O Jogador {res_msg}")
    print(f"O computador jogou {computador} e o jogador {jogador}, resultando em {resultado}")
            
def game():
    vitorias = 0
    while True:
        computador = randint(1, 10)
        jogador = int(input("Digite um número: "))
        escolha = str(input("Escolha Par ou ímpar: [P][I]"))
        resultado = computador + jogador
        if (escolha in 'Pp' and resultado % 2 == 0) or (escolha in 'Ii' and resultado % 2 != 0):
            exibir_resultado(True, computador, jogador, resultado)
            vitorias += 1
        else:
            exibir_resultado(False, computador, jogador, resultado)
            print(f"Total de vitórias consecutivas até derrota: {vitorias}")
            break

if __name__ == "__main__":
    main()