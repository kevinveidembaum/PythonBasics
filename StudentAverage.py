def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media(nota1, nota2)

def media(nota1, nota2):
    media = (nota1+nota2)/2
    print("Média final do aluno: {}".format(media))
    if(media < 6):
        print("Reprovado")
    else:
        print("Aprovado")

main()