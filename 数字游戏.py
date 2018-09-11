if __name__ == '__main__':
    a = int(input())
    b = list(map(int, input().strip().split(" ")))
    # b.sort()
    change = set()
    for i in range(a):
        tmp1 = set()
        tmp2 = set()
        if len(change) != 0:
            for j in change:
                tmp1.add(j + b[i])
        for j in range(i + 1, a):
            tmp2.add(b[i] + b[j])
        change = change.union(tmp1).union(tmp2)

    # print(len(b))
    change = (list(change) + b)
    change.sort()
    i = 0
    j = 1
    while j < len(change) and (change[i] == change[j] or change[j] - change[i] == 1):
        i += 1
        j += 1

    print(change[i] + 1)
    # a = set()
    # a.add(1)
    # a.add(2)
    # b = set()
    # for i in a:
    #     b.add(i + 3)
    #
    # print(a.union(b))
