def getSum(x, A):
    res = 0
    while x > 0:
        res += x % A
        x //= A
    return res


def gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


if __name__ == '__main__':
    A = int(input())
    res = 0
    for i in range(2, A):
        res += getSum(A, i)
    under = A - 2
    gcd_xy = gcd(res, under)

    print(str(res // gcd_xy), "/", str(under // gcd_xy), sep="")
    # print(gcd(6,9))
