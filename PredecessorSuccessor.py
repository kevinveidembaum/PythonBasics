def main():
    n = int(input("Digite um número: "))
    preAfter(n)

def preAfter(n):
    print("Antecessor do número digitado: {}".format(n-1))
    print("Sucessor do número digitado: {}".format(n+1))

main()