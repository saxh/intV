def check(a):
    Odd, Even = False, False
    for i in a:
        if i % 2 == 1:
            Odd = True
        else:
            Even = True
    return Odd and Even


def divid_apple(a):
    if check(a):
        return -1
    if sum(a) % len(a) != 0:
        return -1
    ave_sum = sum(a) / len(a)
    res = 0
    for i in a:
        res += abs(i - ave_sum)
    return res / 4


if __name__ == '__main__':
    a = int(input())
    b = input().split(" ")
    b = [int(b[i]) for i in range(a)]
    print(int(divid_apple(b)))
