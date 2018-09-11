if __name__ == '__main__':
    a = input()
    # print(ord("C") - ord("A"))
    ans = "Likes"
    hash_all = [0] * 26
    for i in range(len(a)):
        hash_all[ord(a[i]) - ord("A")] += 1
    if max(hash_all) >= 4:
        ans = "Dislikes"
        exit()
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            ans = "Dislikes"
            exit()
    need_check = []
    for i in range(len(hash_all)):
        if hash_all[i] >= 2:
            need_check.append(chr(ord("A") + i))
    c = [[-1] * 3 for i in range(len(need_check))]
    for i in range(len(need_check)):
        c[i][0] = a.index(need_check[i], 0)
        c[i][1] = a.index(need_check[i], c[i][0] + 1)
        try:
            c[i][2] = a.index(need_check[i], c[i][1] + 1)
        except:
            pass

    print(a)
