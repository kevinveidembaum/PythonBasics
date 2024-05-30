def main():
    a = input("Digite algo ")
    tipos(a)


def tipos(a):
    print("Tipo primitivo desse valor é ", type(a))
    print("Somente espaços? ", a.isspace())
    print("É número? ", a.isnumeric())
    print("É alfabético? ", a.isalpha())
    print("É alfanumérico? ", a.isalnum())
    print("É capitalizado? ", a.istitle())

main()