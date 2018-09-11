"""
直接插入排序:
时间复杂度：O(n²)
空间复杂度：O(1)
稳定性：稳定
"""


def insert_sort(array=[]):
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array.pop(i))
                break
    return array


"""
希尔排序:
时间复杂度：O(n)
空间复杂度：O(n*logn)
稳定性：不稳定
"""


def shell_sort(array=[]):
    gap = len(array)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(array)):
            for j in range(i % gap, i, gap):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
    return array


"""
简单选择排序
时间复杂度：O(n²)
空间复杂度：O(1)
稳定性：不稳定
"""


def select_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array

"""
堆排序
时间复杂度：O(nlog₂n)
空间复杂度：O(1)
稳定性：不稳定
"""
if __name__ == '__main__':
    print(select_sort([5, 4, 2, 1, 5, 2, 4, 9, 5]))
