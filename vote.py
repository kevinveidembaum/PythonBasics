from datetime import datetime
def main():
    ano_atual = datetime.now().year
    nasc = int(input("Ano de nascimento: "))
    idade = ano_atual - nasc
    print(f"Pessoa com {idade} anos: {voto(idade)}")

def voto(idade):
    if idade < 16:
        return 'VOTO NEGADO'
    elif idade <= 17:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'

if __name__ == "__main__":
    main()