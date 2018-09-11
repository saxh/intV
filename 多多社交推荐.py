if __name__ == '__main__':
    N, SP = list(map(int, input().strip().split(" ")))
    all = [i for i in range(N)]
    # print(all)
    mat = []
    for i in range(N):
        mat.append(list(map(int, input().strip().split(" "))))
    for i in range(len(mat[SP])):
        all.remove(mat[SP][i])

    # if len(all) == 1:
    #     print(all[0])
    #     exit()
    max = 0
    id = -1
    for i in range(len(all)):
        count = 0
        for j in range(len(mat[all[i]])):
            if mat[SP].__contains__(mat[all[i]][j]):
                count += 1
                # print(count)
            if count > max:
                max = count
                id = all[i]
    print(id)
