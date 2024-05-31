from math import trunc
def main():
    real = float(input("Digite um número: "))
    print(f"A parte Inteira do valor {real} corresponde a {trunc(real)}")

if __name__ == "__main__":
    main()