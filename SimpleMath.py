def main():
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite outro valor: "))
    contas(n1, n2)

def contas(n1, n2):
    s = n1+n2
    sub = n1-n2
    m = n1*n2
    d =n1/n2
    div = n1//n2
    e = n1**n2
    print("A soma é {}, subtração é {}, multiplicação é {}, divisão é {:.2f}".format(s, sub, m, d), end=' ')
    print("Divisão inteira é {:.2f} e potência é {:.2f}".format(div, e))

main()