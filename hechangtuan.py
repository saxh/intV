if __name__ == '__main__':
    stu_num = int(input())
    ab = input()
    k, d = input().strip().split(" ")
    k = int(k)
    d = int(d)
    abilities = ab.strip().split(" ")
    abilities = [int(i) for i in abilities]
    # print(abilities)
    max_ab = [[0] * stu_num for i in range(k)]
    min_ab = [[0] * stu_num for i in range(k)]

    # print(max)
    for i in range(stu_num):
        max_ab[0][i] = abilities[i]
        min_ab[0][i] = abilities[i]
    for i in range(1, k):
        for j in range(0, stu_num):
            if j > i - 1:
                tmp_max = (max(max_ab[i - 1][max(0, j - d):j]))
                tmp_min = (min(max_ab[i - 1][max(0, j - d):j]))
                if abs(tmp_min) < tmp_max:
                    tmp_min = tmp_max
                if abilities[j] > 0:
                    max_ab[i][j] = tmp_max * abilities[j]
                    min_ab[i][j] = tmp_min * abilities[j]
                else:
                    max_ab[i][j] = tmp_min * abilities[j]
                    min_ab[i][j] = tmp_max * abilities[j]
    if len(max_ab[k - 1]) == 1:
        res = max_ab[k - 1][0]
    else:
        res = max(max_ab[k - 1])
    print(res)
