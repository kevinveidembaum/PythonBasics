def main():
    print("=" *24)
    print("10 TERMOS DE UMA P.A.")
    print("=" *24)
    primeiro_termo = int(input("Informe o primeiro termo: "))
    razao = int(input("Razão: "))
    decimo = primeiro_termo + (10-1) * razao
    for x in range(primeiro_termo, decimo+razao, razao):
        print(x, end=" -> ")
    print("Acabou!")

if __name__ == "__main__":
    main()