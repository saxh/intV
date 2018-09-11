if __name__ == '__main__':
    a = input()
    lens = len(a)
    if lens < 6:
        print(a)
    elif lens < 14:
        print(" ".join([a[0:6], a[6:]]))
    else:
        print(" ".join([a[0:6], a[6:14], a[14:]]))
