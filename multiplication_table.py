def main():
    tabuada()

def tabuada():
    while True:
        num = int(input("Quer ver a tabuada de qual número: "))
        if num < 0:
            print("Programa encerrado com sucesso!")
            break
        for x in range(1, 11):
            print(f"{x} x {num} = {x*num}")

if __name__ == "__main__":
    main()