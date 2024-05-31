from math import sqrt, trunc

def main():
    co = float(input("Digite o comprimeno do cateto oposto: "))
    ca = float(input("Digite o comprimeno do cateto adjascente: "))
    print(f"O valor do comprimento da hipotenusa é {trunc(sqrt(co**2 + ca**2))}")    

if __name__ == "__main__":
    main()