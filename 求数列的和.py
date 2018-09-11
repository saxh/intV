if __name__ == '__main__':
    n, m = map(int, input().split(" "))
    res = n
    for i in range(1, m):
        n = n ** 0.5
        res += n
    print("{:.2f}".format(res))
