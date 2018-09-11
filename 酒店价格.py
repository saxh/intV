import sys


def merge(x=[[2, 3, 100], [1, 1, 100], [4, 5, 110]]):
    x.sort(key=lambda x: x[0])
    # print(dateRangePrices)
    # for i in range(len(x) - 1):
    #     if x[i][0] == x[i + 1][0]:
    #         x[i][1] = x[i + 1][0] - 1
    for i in range(len(x) - 1):
        if x[i][1] >= x[i + 1][0]:
            x[i][1] = x[i + 1][0] - 1

    for i in range(len(x) - 1, 0, -1):
        if x[i][0] == x[i - 1][1] + 1 and x[i][2] == x[i - 1][2]:
            x[i - 1][1] = x[i][1]
            x.pop(i)
    # for i in range(len(x)):
    print(",".join(map(str, x)))


if __name__ == '__main__':
    # for i in sys.stdin.readlines():
    #     if i == "":
    #         break
    #     print(i)
    x = []
    while True:
        try:
            cin = input()
            if cin == '':
                break
            s = list(map(int, cin.split(" ")))
            x.append(s)
        except:
            break
    merge(x)
