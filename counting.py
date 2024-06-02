from time import sleep
def main():
    for x in range(10, -1, -1):
        print(x)
        sleep(0.75)
    print("DONE!")


if __name__ == "__main__":
    main()