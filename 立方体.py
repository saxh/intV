if __name__ == '__main__':
    n, k = list(map(int, input().split(" ")))
    ls = list(map(int, input().split(" ")))
    # ls.sort()
    count = 0

    while count <= k:
        min_ls = min(ls)
        max_ls = max(ls)
        mx_count = ls.count(max_ls)
        min_count = ls.count(min_ls)
        if mx_count > min_count:
            if min_count + count > k:
                break
            else:
                count = count + min_count
            index_min = [i for i in range(len(ls)) if ls[i] == min_ls]
            index_max = [i for i in range(len(ls)) if ls[i] == max_ls]

            for i in range(len(index_min)):
                ls[index_min[i]] += 1
                ls[index_max[i]] -= 1
                print(index_max[i], index_min[i])
        else:
            if mx_count + count > k:
                break
            else:
                count = count + mx_count
            index_min = [i for i in range(len(ls)) if ls[i] == min_ls]

            index_max = [i for i in range(len(ls)) if ls[i] == max_ls]
            for i in range(len(index_max)):
                ls[index_max[i]] -= 1
                ls[index_min[i]] += 1
                print(index_max[i], index_min[i])
