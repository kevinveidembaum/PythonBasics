DIAS_PRECO = 60
KM_PRECO = 0.15

def main():
    aluguel_carro()

def aluguel_carro():
    dias = int(input("Quantos dias o carro foi alugado: "))
    km = float(input("Quantos Km's foram rodados: "))

    totalPagar = (DIAS_PRECO*dias)+(KM_PRECO*km)
    print(f"Total a pagar: R${totalPagar:.2f}")

if __name__ == "__main__":
    main()