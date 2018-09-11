def f(x):
    x = list(map(int, list(str(x))))
    return sum(x)


def g(x):
    count = 0
    while x:
        x &= (x - 1)
        count += 1
    return count


if __name__ == '__main__':
    a = int(input())
    res = 0
    for i in range(1,a + 1):
        if g(i) == f(i):
            res += 1
    print(res)
