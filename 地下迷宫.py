if __name__ == '__main__':
    n, m, p = list(map(int, input().strip().split(" ")))
    pazzle = []
    for i in range(n):
        pazzle.append(list(map(int, input().strip().split(" "))))
    pd = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            pazzle[m][n]