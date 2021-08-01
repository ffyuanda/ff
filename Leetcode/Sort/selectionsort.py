""" self-realized selection sort python version """
# https://www.youtube.com/watch?v=GUDLRan2DWM


def find_min_index(a: list, start: int) -> int:
    min_ = float('inf')
    min_i = 0
    for i in range(start, len(a)):
        if a[i] <= min_:
            min_ = a[i]
            min_i = i
    return min_i


def selectionsort(a: list) -> list:
    count = 0

    while count < len(a):
        min_i = find_min_index(a, count)
        a[count], a[min_i] = a[min_i], a[count]
        count += 1

    return a


print(selectionsort([2, 3, 1, 4, 7, 5]))
