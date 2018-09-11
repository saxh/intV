if __name__ == '__main__':
    a = int(input())
    begin = -90
    end = 90
    mid = 0
    res = []
    while end - begin >= 5:
        mid = int((begin + end) / 2)
        if a >= mid:
            res.append("1")
            begin = mid
        else:
            res.append("0")
            end = mid
    print("".join(res))
    # print(-3//2)
    # print(int(-3/2))
