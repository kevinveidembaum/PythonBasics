def main():
    lista = list()
    for count in range(0, 5):
        lista.append(int(input(f"Digite um valor para a posição {count}: ")))
    
    print(f"Você digitou os valores {lista}.")
    print(f"O maior número foi o {max(lista)} e ele apareceu {lista.count(max(lista))} vezes nas posições ", end='')
    for i, v in enumerate(lista):   #Pega a posição/indíce do maior número da lista
        if v == max(lista):
            print(i, end=' ')

    print(f"\nO menor número foi o {min(lista)} e ele apareceu {lista.count(min(lista))} vezes nas posições ", end='')
    for i, v in enumerate(lista):   #Pega a posição/indíce do menor número da lista
        if v == min(lista):
            print(i, end=' ')

if __name__ == "__main__":
    main()