if __name__ == '__main__':
    a = int(input())
    x, y = 0, 1

    while y < a:
        tmp = x + y
        x = y
        y = tmp
    print(min([a - x, y - a]))
