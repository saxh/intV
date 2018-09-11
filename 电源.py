if __name__ == '__main__':
    n, p1, p2, p3, t1, t2 = list(map(int, input().split(" ")))
    lr = []
    for i in range(n):
        lr.append(list(map(int, input().split(" "))))
    res = 0
    for i in lr:
        res += (i[1] - i[0]) * p1
    for i in range(len(lr) - 1):
        if lr[i + 1][0] - lr[i][1] >= t1 + t2:
            res += t1 * p1 + t2 * p2 + (lr[i + 1][0] - lr[i][1] - t1 - t2) * p3
        elif lr[i + 1][0] - lr[i][1] >= t1:
            res += t1 * p1 + (lr[i + 1][0] - lr[i][1] - t1) * p2
        elif lr[i + 1][0] - lr[i][1] >= 0:
            res += (lr[i + 1][0] - lr[i][1]) * p1
        else:
            res += (lr[i + 1][0] - lr[i][1]) * p1
    print(res)
