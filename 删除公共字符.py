if __name__ == '__main__':
    a = input()
    b = input()

    for i in b:
        a = "".join(a.split(i))
    print(a)
