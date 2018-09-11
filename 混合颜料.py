# def getHighPosition(number):
#     count = 0
#     while number > 0:
#         number = number >> 1
#     count += 1
#     return count
# n = int(input())
# colors = list(map(int, input().split()))
# colors.sort()
# # 分别记录最后两个数的下标(最大的两个数)
# lastIndex = len(colors) - 1
# bLastIndex = lastIndex - 1
# num = 0
# while len(colors) > 2:
#     if getHighPosition(colors[lastIndex]) == getHighPosition(colors[bLastIndex]):
#         temp = colors[lastIndex] ^ colors[bLastIndex]
#     if not colors.__contains__(temp):
#         colors.append(temp)  # 需要使用append而不是add
#         colors.sort()
#         lastIndex += 1
#         bLastIndex += 1
#     else:
#         num += 1
#         colors.pop()
#         lastIndex -= 1
#         bLastIndex -= 1
# print(num + len(colors))
if __name__ == '__main__':
    n = int(input())
    ls = list(map(int, input().split(" ")))
    for i in range(n - 1):
        ls[i + 1:] = sorted(ls[i + 1:])
        for j in range(i + 1, n):
            if ls[j] ^ ls[i] < ls[j]:
                ls[j] ^= ls[i]
    # print(ls)
    print(n - ls.count(0))
