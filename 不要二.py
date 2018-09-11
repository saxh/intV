if __name__ == '__main__':
    a, b = list(map(int, input().strip().split(" ")))
    print(a, b)
    k1 = int(a / 4) + 1
    r1 = a % 4
    k2 = int(b / 4)
    r2 = b % 4
    sum_row0 = k1 * 2
    if r1 == 1:
        sum_row0 -= 1
    sum = (a - sum_row0) * k2 * 2 + sum_row0 * k2 * 2
    if r2 <= 2:
        sum = sum + r2 * sum_row0
    else:
        sum = sum + 2 * sum_row0 + (a - sum_row0)
    print(sum)
