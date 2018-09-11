if __name__ == '__main__':
    N2M = input().strip()
    a = input().strip()
    b = input().strip()
    count_a = N2M.count(a)
    count_b = N2M.count(b)
    if a == b and count_a >=2:
        print("both")
        exit()
    if count_a == 0 or count_b == 0:
        print("invalid")
        exit()
    sp = N2M.split(a)
    # if sp[0] == "":
    #     print("forward")
    #     exit()
    # elif sp[-1] == "":
    #     print("backward")
    #     exit()

    count = 0
    index = []
    for i in range(len(sp)):
        if sp[i].__contains__(b):
            count += 1
            index.append(i)
    if count == 0:
        print("invalid")
        exit()
    if count == 1 and index[0] == 0:
        print("backward")
    elif count == 1 and index[0] == len(sp) - 1:
        print("forward")
    else:
        print("both")
