def main():
    santo()

def santo():
    cidade = str(input("Cidade a qual você mora: ")).strip()
    print(cidade[:5].upper() == 'SANTO')

if __name__ == "__main__":
    main()