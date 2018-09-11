def jiecheng(x):
    tmp = 1
    for i in range(1, x + 1):
        tmp *= i
    return tmp


if __name__ == '__main__':
    x, y = list(map(int, input().strip().split(" ")))
    s = x + y
    print(int(jiecheng(s) / jiecheng(x) / jiecheng(y)))
