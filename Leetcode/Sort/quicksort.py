""" self-realized quicksort python version """
# https://www.youtube.com/watch?v=COk73cpQbFQ


def partition(l: list, start: int, end: int, reverse: bool = False):
    # last element as pivot
    pivot = l[end]
    pIndex = start
    for i in range(start, end):
        if reverse:

            if l[i] >= pivot:
                # swap larger ones to left of the pIndex
                l[pIndex], l[i] = l[i], l[pIndex]
                pIndex += 1
        else:

            if l[i] <= pivot:
                # swap smaller ones to left of the pIndex
                l[pIndex], l[i] = l[i], l[pIndex]
                pIndex += 1
    # swap the pivot
    l[pIndex], l[end] = l[end], l[pIndex]
    return pIndex


def quicksort(l: list, start: int, end: int):

    if start >= end:
        return
    pIndex = partition(l, start, end)
    quicksort(l, start, pIndex-1)
    quicksort(l, pIndex+1, end)


c = [2, 1, 3, 4, 8, 10, 7, 6]
quicksort(c, 0, len(c)-1)
print(c)
