import urllib.request
def main():
    
    try:
        site = urllib.request.urlopen("https://www.google.com/")
    except urllib.error.URLError:
        print("Erro na conexão com a internet ou a URL não foi encontrada")
    else:
        print("Conexão estabelecida com sucesso!")

if __name__ == "__main__":
    main()