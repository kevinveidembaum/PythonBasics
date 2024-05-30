def main():
    num = int(input("Digite um número para ver sua tabuada: "))
    tabuada(num)

def tabuada(n):
    x = 1;
    for x in range(11):
        print("{} X {} = {}".format(n, x, n*x))

main()