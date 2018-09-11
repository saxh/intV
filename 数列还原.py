def getSum(data):
    sum = 0
    for i in range(0, len(data) - 1):
        for j in range(i, len(data)):
            if data[i] * data[j] != 0 and data[i] < data[j]:
                sum += 1
    return sum


def deal(stack):
    # pass
    global c, b, ans
    tmp = c[:]
    i = 0
    j = 0
    while i < len(tmp):
        if tmp[i] == 0:
            tmp[i] = stack[j]
            i += 1
            j += 1
        else:
            i += 1
    if getSum(tmp) == b:
        ans += 1
        print(stack)


# def dfs(rest):
#     stack = []
#     visited = len(rest) * [False]
#     arr = []
#
#     for i in range(len(rest)):
#         visited[i] = True
#         stack.append(rest[i])
#         while len(stack) > 0:
#             is_push = False
#             if len(stack) == len(rest):
#                 deal(stack)
#             for j in range(len(rest)):
#                 if visited[j] is not True:
#                     stack.append(rest[j])
#                     visited[j] = True
#                     is_push = True
#                     break
#             if is_push is not True:
#                 stack.pop()
#                 visited[j] = False
def dfs(rest, flag, index, length, stack):
    if index == length:
        deal(stack)
        return
    for i in range(length):
        if flag[i] is not True:
            flag[i] = True
            stack.append(rest[i])
            dfs(rest, flag, index + 1, length, stack)
            stack.pop()
            flag[i] = False


if __name__ == '__main__':
    a, b = input().strip().split(" ")
    a, b = int(a), int(b)
    c = list(map(int, input().strip().split(" ")))
    ans = 0
    # c = [int(i) for i in input().strip().split(" ")]
    # print(a, b)
    # print(c)


    rest = [i for i in range(1, a + 1)]
    for i in c:
        if i != 0:
            rest.remove(i)
    print(rest)
    flag = [False] * len(rest)
    stack = []
    dfs(rest, flag, 0, len(rest), stack)
    print(ans)
# def getsum(data):
#     sum = 0
#     for i in range(len(data) - 1):
#         for j in range(i + 1, len(data)):
#             if data[i] * data[j] != 0 and data[i] < data[j]:
#                 sum += 1
#     return sum
#
#
# def gets(data, index, num):
#     sum = 0
#     for i in range(index):
#         if data[i] < num:
#             sum += 1
#     for i in range(index + 1, len(data)):
#         if data[i] > num:
#             sum += 1
#     return sum
#
#
# def deal(__data):
#     global data, ssum, k, ans
#     temp = [item for item in data]
#     index, sum = 0, 0
#     for i in range(len(__data)):
#         while temp[index] != 0:
#             index += 1
#         temp[index] = __data[i]
#         sum += gets(temp, index, temp[index])
#     if ssum + sum == k:
#         ans += 1
#
#
# def allshow(__data, flag, end, leng):
#     global _data
#     if end == leng:
#         deal(__data)
#         return
#     for i in range(leng):
#         if flag[i] == 0:
#             flag[i] = 1
#             __data[end] = _data[i]
#             allshow(__data, flag, end + 1, leng)
#             flag[i] = 0
#
#
# n, k = list(map(int, input().split()))
# data = list(map(int, input().split()))
# ans, ssum = 0, getsum(data)
# _data = list(range(1, n + 1))
# for i in range(n):
#     if data[i] != 0 and data[i] in _data:
#         _data.remove(data[i])
# allshow([0 for i in range(len(_data))], [0] * len(_data), 0, len(_data))
# print(ans)
