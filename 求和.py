def dfs(index, m, tmp=[]):
    if m < 0:
        return
    if m == 0:
        print(" ".join(list(map(str, tmp))))
        return
    for i in range(index, n + 1):
        tmp.append(i)
        dfs(i + 1, m - i, tmp)
        tmp.pop(-1)


if __name__ == '__main__':
    n, m = list(map(int, input().split(" ")))
    dfs(1, 5)
