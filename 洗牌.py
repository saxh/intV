def shuffle(ls, len):
    tmp = [0] * 2 * len
    for j in range(len):
        tmp[j * 2] = ls[j]
        tmp[j * 2 + 1] = ls[j + len]
    return tmp


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        data = list(map(int, input().strip().split(" ")))
        n, k = data[0], data[1]
        ls = data[2:]
        k = k % 4
        res = ls
        for j in range(k):
            res = shuffle(res, n)
            # print(res)
            # for j in range(len(res)):
            #     # print(res[j], end=" ")
            #     final_res += str(res[j])
            #     final_res += " "
            #     # for i in range(len(final_res)-1):

        print(" ".join(map(str, res)))
# 3
# 3 1 1 2 3 4 5 6
# 3 2 1 2 3 4 5 6
# 2 2 1 1 1 1

