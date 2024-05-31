from random import choice
def main():
    lista = []
    
    for x in range(5):
        aluno = str(input(f"{x+1}º Aluno: "))
        lista.append(aluno)

    escolha = choice(lista)
    print(f"O aluno escolhido foi {escolha}")
    
if __name__ == "__main__":
    main()