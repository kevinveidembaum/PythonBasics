def main():
    completa = [[], []]
    for i in range(0, 7):
        num = int(input(f"Digite o {i+1}° número: "))
        if num % 2 == 0:
            completa[0].append(num)
        else:
            completa[1].append(num)
    completa[0].sort()
    completa[1].sort()
    print(f"Os valores pares catalogados foram: {completa[0]}")
    print(f"Os valores ímpares catalogados foram: {completa[1]}")

if __name__ == "__main__":
    main()