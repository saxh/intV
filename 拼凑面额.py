def dfs(N, index):
    global res

    if N < 5:
        res += 1
        return
    if index == 5:
        res += 1
        return
    count = N // money_type[index]
    for i in range(count + 1):
        dfs(N - i * money_type[index], index + 1)


if __name__ == '__main__':
    res = 0
    money_type = [100, 50, 20, 10, 5, 1]
    N = int(input().strip())
    dfs(N, 0)
    print(res)
