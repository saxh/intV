if __name__ == '__main__':
    n = int(input())
    ls = list(map(int, input().strip().split(" ")))
    ls.sort()
    remain = []
    index = 0
    while index < n - 2:
        if ls[index] >= ls[index + 1] - 10 and ls[index + 1] >= ls[index + 2] - 10:
            index += 3
        else:
            remain.append(ls[index])
            index += 1
            if index == n - 3:
                remain.append(ls[-1])
                remain.append(ls[-2])
    for i in range(len(remain)):
        if remain[i]<remain[i]
