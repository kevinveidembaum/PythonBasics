TAXA_DESCONTO = 0.05

def main():
    preco = float(input("Digite o valor do produto: R$"))
    desconto(preco)

def desconto(preco):
    if(preco > 100.00):
        d = preco * TAXA_DESCONTO
        preco -= d
        print(f"Desconto de {int(TAXA_DESCONTO*100)}% aplicado. Novo preço: R$ {preco:.2f}")
    else:
        print("Infelizmente o produto não recebe desconto.")

if __name__ == "__main__":
    main()