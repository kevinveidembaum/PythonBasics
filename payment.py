TAXA_DESCONTO_1 = 0.1
TAXA_DESCONTO_2 = 0.05
TAXA_JUROS = 0.2

def main():
    preco = float(input("Preço total da sua compra: "))
    escolha = int(input("""Escolha a forma de pagamento
    [1]à vista
    [2]à vista no cartão
    [3]2x no cartão
    [4]3x ou mais no cartão
    """))
    pagamento(preco, escolha)

def pagamento(preco, escolha):
    if(escolha == 1):
        print(f"Recebeu desconto de {int(TAXA_DESCONTO_1*100)}%")
        print(f"Sua compra de R${preco:.2f} irá custar R${preco - (preco*TAXA_DESCONTO_1):.2f} à vista.")
    elif(escolha == 2):
        print(f"Recebeu desconto de {int(TAXA_DESCONTO_2*100)}%")
        print(f"Sua compra de R${preco:.2f} irá custar R${preco - (preco*TAXA_DESCONTO_2):.2f} à vista no cartão")
    elif(escolha==3):
        print("Não recebe desconto. Preço normal.")
        print(f"Sua compra irá custar R${preco:.2f} em 2x no cartão. Cada parcela: R${preco/2:.2f}")
    elif(escolha==4):
        print(f"Recebeu taxa de juros de {int(TAXA_JUROS*100)}%")
        parcelas = int(input("Em quantas parcelas deseja pagar: "))
        neo_preco = preco + (preco * TAXA_JUROS)
        print(f"Sua compra de R${preco:.2f} irá custar R${neo_preco:.2f}")
        print(f"Sua compra será parcelada em {parcelas}x de R${(neo_preco/parcelas):.2f}.")

if __name__ == "__main__":
    main()