def depth(x=[]):
    if len(x) == 0:
        return 1
    res = []
    for i in range(2):
        res.append(depth(R[x[i]]) + 1)
    return max(res)


if __name__ == '__main__':
    n = int(input())
    R = [[] for i in range(n)]
    for i in range(n - 1):
        tmp = list(map(int, input().split(" ")))
        R[tmp[0]].append(tmp[1])
    print(depth(R[0]))
