from math import sqrt
def main():
    n = raiz_quadrada()
    print(f"Raiz quadrada do número: {n}")

def raiz_quadrada():
    num = int(input("Digite um número: "))
    return sqrt(num)

if __name__ == "__main__":
    main()