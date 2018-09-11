if __name__ == '__main__':
    n, m = list(map(int, input().strip().split(" ")))
    ls = list(map(int, input().strip().split(" ")))
    res = 0
    for i in range(n):
        for j in range(n):
            if ls[i] ^ ls[j] > m:
                res += 1
    print(res/2)
    print(-1^1)