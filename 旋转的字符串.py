if __name__ == '__main__':
    a = list(input())
    # print(len(a))
    K = len(a) // 4
    mat = [[" "] * (K + 1) for i in range(K + 1)]
    for i in range(K + 1):
        mat[0][i] = a[i]
    for i in range(K + 1):
        mat[-1][i] = a[2 * K + i]
    mat[-1].reverse()
    for i in range(1, K):
        mat[i][-1] = a[K + i]
    for i in range(1, K):
        mat[i][0] = a[4*K - i]
    for i in range(len(mat)):
        print("".join(mat[i]))
    # print(mat)
