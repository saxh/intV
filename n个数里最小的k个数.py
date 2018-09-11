def insert(num):
    global k, k_min
    if len(k_min) < k:
        k_min.append(num)
        k_min.sort()
    else:
        k_min.append(num)
        k_min.sort()
        del k_min[-1]


if __name__ == '__main__':
    a = list(map(int, input().strip().split(" ")))
    k = a[-1]
    del a[-1]
    k_min = [a[0]]
    for i in range(1, len(a)):
        if a[i] < k_min[-1] or len(k_min) < k:
            insert(a[i])
    # print(k_min)
    res = ' '.join(list(map(str, k_min)))
    # for i in range(k):
    #     if i != k - 1:
    #         res += str(k_min[i]) + " "
    #     else:
    #         res += str(k_min[i])
    print(res)
