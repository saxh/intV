if __name__ == '__main__':
    match = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    M, N = list(map(int, input().split(" ")))
    Flag = True
    if M < 0:
        Flag = False
        M = abs(M)
    res = []
    while M > 0:
        res.append(match[M % N])
        M = M // N
    if Flag is not True:
        res.append("-")
    res.reverse()
    print("".join(res))
