def main():
    print("~~"*12)
    print("Sequência de Fibonnaci")
    print("~~"*12)
    n = int(input("Digite quantos números você quer visualizar: "))
    fib(n)

def fib(n):
    t1 = 0
    t2 = 1
    print(f"{t1} -> {t2}", end='')
    c = 3
    while c <= n:
        t3 = t2 + t1
        print(f" -> {t3}", end='')
        t1 = t2
        t2 = t3
        c += 1

if __name__ == "__main__":
    main()