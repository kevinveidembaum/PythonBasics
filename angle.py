from math import sin, cos, tan, radians
def main():
    angulo = float(input("Digite um ângulo: "))
    angles(angulo)

def angles(angulo):
    seno = sin(radians(angulo))
    cosseno = cos(radians(angulo))
    tangente = tan(radians(angulo))
    print(f"Valor de Seno é {seno:.2f}, Cosseno é {cosseno:.2f} e Tangente é {tangente:.2f}")

if __name__ == "__main__":
    main()