def main():
    palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

    for p in palavras:
        print(f'\nNa palavra {p} temos as vogais: ', end='')
        for letras in p:
            if letras.upper() in 'AEIOU':
                print(f'{letras}', end=' ')

if __name__ == "__main__":
    main()