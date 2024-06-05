def main():
    lista = []
    expressao = str(input("Digite uma expressão matemática: "))
    for parentese in expressao:
        if parentese == '(':
            lista.append('(')
        elif parentese == ')':
            if len(lista) > 0:
                lista.pop()
            else:
                lista.append(')')
                break

    if len(lista) == 0:
        print("Expressão válida.")
    else:
        print("Expressão inválida.")

if __name__ == "__main__":
    main()