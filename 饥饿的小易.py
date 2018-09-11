if __name__ == '__main__':
    a = int(input())
    count = 0
    while a % 1000000007 != 0:
        count += 1
        a = 2 * a + 1
    if count % 3 == 0:
        print(count // 3)
    elif count % 3 == 1:
        print((count - 4) // 3 + 2)
    else:
        print(count // 3 + 1)
