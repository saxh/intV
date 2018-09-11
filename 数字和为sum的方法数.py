if __name__ == '__main__':
    n, sum = list(map(int, input().strip().split(" ")))
    nums = list(map(int, input().strip().split(" ")))
    nums = [i for i in nums if i <= sum]
    nums.sort()
    dp = [0] * (sum + 1)
    for i in range(len(nums)):
        dp[nums[i]] += 1
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] <= sum:
                    dp[nums[i] + nums[j]] += dp[nums[i]] * dp[nums[j]]
    print(dp[sum])
