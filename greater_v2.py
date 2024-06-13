def main():
    maior(23, 43, 4)
    maior(2, 3)
    maior(4, 5, 19, -13)

def maior(* num):
    sorted(num, reverse=True)
    print("~" * 40)
    print(f"Foram informados os valores {num}, ao todo {len(num)} valores")
    print(f"E o maior valor informado foi {num[0]}")
    print("~" * 40)

if __name__ == "__main__":
    main()