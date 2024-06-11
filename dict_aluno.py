def main():
    aluno = dict()
    aluno['nome'] = str(input("Digite o nome do aluno: "))
    aluno['media'] = float(input("Digite a media do aluno: "))
    if aluno['media'] < 5:
       aluno['situacao'] = 'Reprovado'
    if aluno ['media'] <= 6:
       aluno['situacao'] = 'Recuperação'
    if aluno['media'] > 6:
       aluno['situacao'] = 'Aprovado'

    print(f"Aluno {aluno['nome']} teve média de {aluno['media']} e está {aluno['situacao']}")

if __name__ == "__main__":
  main()

