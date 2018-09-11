if __name__ == '__main__':
    a = list(input())
    a.reverse()
    try:
        index = a.index(".")
        b = a[:index]
        b.reverse()
        print("".join(b))
    except:
        print("null")