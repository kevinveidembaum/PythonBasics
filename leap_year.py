from datetime import date
def main():
    ano = int(input('Digite qualquer ano ou digite 0 para pegar o ano atual: '))
    year(ano)

def year(ano):
    if(ano == 0):
        ano = date.today().year

    if ano % 4 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano {ano} é BISSEXTO!")
    else:
        print(f"O ano {ano} NÃO É BISSEXTO!")

if __name__ == "__main__":
    main()