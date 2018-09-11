if __name__ == '__main__':
    a = int(input())
    if a == 6:
        print(1)
        exit()
    elif a < 8:
        print(-1)
        exit()

    dp = [-1] * (a + 1)
    dp[8] = 1
    dp[6] = 1
    for i in range(6, a + 1):
        if dp[i - 6] != -1 and dp[i - 8] != -1:
            dp[i] = min(dp[i - 6] + 1, dp[i - 8] + 1)
        elif dp[i - 6] != -1:
            dp[i] = dp[i - 6] + 1
        elif dp[i - 8] != -1:
            dp[i] = dp[i - 8] + 1
    print(dp[a])
