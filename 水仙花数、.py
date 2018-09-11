if __name__ == '__main__':
    m, n = list(map(int, input().split(" ")))
    res = []
    for i in range(m, n + 1):
        a = i % 10
        b = i // 10 % 10
        c = i // 100 % 10
        if a ** 3 + b ** 3 + c ** 3 == i:
            res.append(i)
    if len(res) == 0:
        print("no")
    else:
        print(" ".join(map(str, res)))
