if __name__ == '__main__':
    a = list(map(int, input().strip().split(" ")))
    max_a = max(a)
    dp = [0] * max_a
    dp[0] = 3
    dp[1] = 9
    for i in range(2, max_a):
        dp[i] = dp[i - 1] * 2 + dp[i - 2]

    res = []
    for i in a:
        res.append(str(dp[i - 1]))
    str = " ".join(res)
    print(str)
