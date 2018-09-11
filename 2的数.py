# def partition(start, end, a):
#     pivot = a[end]
#     i, j = start, end - 1
#     while i < j:
#
#         while a[i] < pivot:
#             i += 1
#         while a[j] > pivot:
#             j -= 1
#         if i < j:
#             a[i], a[j] = a[j], a[i]
#     a[end] = a[i]
#     a[i] = pivot
#     return i
#
#
# def sort(l, r, a):
#     if l >= r:
#         return
#     mid = partition(l, r, a)
#     if mid > (l + r) // 2:
#         sort(l, mid - 1, a)
#     else:
#         sort(mid + 1, r, a)
#
#
# if __name__ == '__main__':
#     a = [1, 7, 2, 4, 6, 2, 3, 4, 1, 6, 8, 10, 2222]
#     sort(0, len(a) - 1, a)
#     print(a)
if __name__ == '__main__':
    a = sorted(list(map(int, input().strip().split(' '))))
    if len(a) % 2 == 1:
        print(a[len(a) // 2])
    else:
        if a[len(a) // 2] == a[-1]:
            print(a[-1])
        else:
            print(a[len(a) // 2-1])
