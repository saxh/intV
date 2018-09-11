if __name__ == '__main__':
    n = int(input())
    J = list(map(int, input().split(" ")))
    dp = [9999] * (n + 1)
    dp[0] = 0
    for i in range(n):
        dp[i:i + J[i] + 1] = [min(j, dp[i] + 1) for j in dp[i:i + J[i] + 1]]
    if dp[-1] != 9999:
        print(dp[-1])
    else:
        print(-1)
