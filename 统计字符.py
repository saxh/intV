if __name__ == '__main__':
    a = input()
    # a = "".join(a.split(" "))
    # count = {}
    # for i in a:
    #     if i.isalpha() or i.isdigit():
    #         try:
    #
    #             count[i] += 1
    #             if count[i] == 3:
    #                 print(i)
    #                 break
    #         except:
    #             count[i] = 1
    count = {}
    for i in a:
        if i.isalpha():
            count[i] = count.setdefault(i, 0) + 1
            if count[i] == 3:
                print(i)
                break
