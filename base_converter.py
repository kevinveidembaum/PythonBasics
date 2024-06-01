def main():
    n = int(input("Digite um número para ser convertido: "))
    escolha = int(input("""Escolha um tipo de Conversão: 
    [1] BINÁRIO [2] OCTAL [3] HEXADECIMAL 
    """))
    conversor(n, escolha)

def conversor(numero, escolha):
    if(escolha == 1):
        print(f"O valor de {numero} em binário corresponde a {bin(numero)[2:]}")
    elif(escolha == 2):
        print(f"O valor de {numero} em octal corresponde a {oct(numero)[2:]}")
    elif(escolha == 3):
        print(f"O valor de {numero} em hexadecimal corresponde a {hex(numero)[2:]}")
    else:
        print("Informe um valor válido.")

if __name__ == "__main__":
    main()