def inputDinheiro(msg):
    valid = False
    while not valid:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print("ERRO. Digite um valor válido")
        else:
            valid = True
            return float(entrada)
