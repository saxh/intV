if __name__ == '__main__':
    a = int(input())
    sqrt_a = a ** 0.5
    x1 = 0
    ans = 0
    while x1 <= sqrt_a:
        rest = a - x1 ** 2
        x2 = (a - x1 ** 2) ** 0.5
        if int(x2) ** 2 == rest:
            if x1 == 0 or x2 == 0:
                ans += 2
            else:
                ans += 4
        x1 += 1
    print(ans)