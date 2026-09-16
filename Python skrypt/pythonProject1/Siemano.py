def nwd(a,b):
    while(a != b):
        if a > b:
            a = a-b
        else:
            b = b-a
    return a


def main():
    a=int(input("Wprowadź wartość a"))
    while a < 1:
        print("Wartość musi być dodatnia")
        a = int(input("Wprowadź wartość a"))
    b=int(input("Wprowadź wartość b"))
    while b <= 0:
        print("Wartość musi być dodatnia")
        b = int(input("Wprowadź wartość b"))

    print(nwd(a,b))



if __name__=="__main__":
    main()