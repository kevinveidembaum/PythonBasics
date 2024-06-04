from random import randint
def main():
    aleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
    print("Números que foram gerados aleatorimente: ", end='')
    for n in range(0, 5):
        print(aleatorios[n], end=' ')

    print(f"\nMenor valor gerado: {sorted(aleatorios)[0]}") #max(aleatorios)
    print(f"\Maior valor gerado: {sorted(aleatorios)[-1]}") #min(aleatorios)


if __name__ == "__main__":
    main()