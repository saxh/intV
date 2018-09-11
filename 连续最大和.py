if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split(" ")))
    # print(len(a))
    # del a[0]

    dp = [0] * (n)
    dp[0] = a[0]
    for i in range(1, n):
        if dp[i - 1] < 0:
            dp[i] = a[i]
        else:
            dp[i] = a[i] + dp[i - 1]
    print(max(dp))
