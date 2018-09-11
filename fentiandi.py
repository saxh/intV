if __name__ == '__main__':
    n, m = input().strip().split(" ")
    m = int(m)
    n = int(n)
    sum_mat = [[0] * m for i in range(n)]
    print(sum_mat)
    mat = [[0] * m for i in range(n)]
    for i in range(n):
        s = input()
        for j in range(m):
            mat[i][j] = int(s[j])
            if j >= 1:
                sum_mat[i][j] = sum_mat[i - 1][j] + sum_mat[i][j - 1] - sum_mat[i - 1][j - 1] + mat[i][j]
            else:
                sum_mat[i][j] = mat[i][j] + sum_mat[i - 1][j]
    print(sum_mat)
