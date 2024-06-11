from datetime import datetime
def main():
    ano_atual = datetime.now().year
    pessoa = dict()
    pessoa['nome'] = str(input("Digite o nome da pessoa: "))
    pessoa['nasc'] = int(input("Ano de Nascimento: "))
    pessoa['ctps'] = int(input("Carteira de Trabalho: ([0] caso não houver)"))
    pessoa['idade'] = ano_atual - pessoa['nasc']
    if pessoa["ctps"] != 0:
        pessoa['contrato'] = int(input("Ano da Contratação: "))
        pessoa['salario'] = float(input("Salário: "))
        pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contrato'] + 35) - ano_atual)
    
    print('-=' *30)
    for k, v in pessoa.items():
        print(f"{k}: {v}")
    

if __name__ == "__main__":
    main()