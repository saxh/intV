if __name__ == '__main__':
    k = int(input())
    ls = []
    ans = "none"
    length = True
    lexicographically = True
    for i in range(k):
        ls.append(input())
    for i in range(k - 1):
        if len(ls[i]) > len(ls[i + 1]):
            length = False
        len_a = len(ls[i])
        len_b = len(ls[i + 1])
        lens = min([len_a, len_b])
        j = 0
        while j < lens - 1 and ls[i][j] == ls[i + 1][j]:
            j += 1
        if ls[i][j] > ls[i + 1][j]:
            lexicographically = False
        elif ls[i][j] == ls[i + 1][j]:
            if len_b<len_a:
                lexicographically = False
        if length and lexicographically is not True:
            break
    if length and lexicographically:
        ans = "both"
    elif length:
        ans = "lengths"
    elif lexicographically:
        ans = "lexicographically"
    print(ans)
