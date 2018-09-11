if __name__ == '__main__':
    begin, end = list(map(int, input().strip().split(" ")))
    memo = [0] * (end + 1)
    for i in range(begin, end + 1):
        min = i / 3 * 2
        tmp = 99999
        for j in range(int(max([min,begin])), i - 1):

            if j % (i - j) == 0:
                if tmp > memo[j] + 1:
                    tmp = memo[j] + 1
        memo[i] = tmp
    if memo[end] != 99999:
        print(memo[end] - memo[begin])
    else:
        print(-1)
