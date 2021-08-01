""" self-realized mergesort python version """
# https://www.youtube.com/watch?v=TzeBrDU-JaY&t=232s


def merge(a: list, b: list) -> list:
    merged = []
    ai, bi = 0, 0
    while ai < len(a) and bi < len(b):
        if a[ai] <= b[bi]:
            merged.append(a[ai])
            ai += 1
        else:
            merged.append(b[bi])
            bi += 1

    # put in the remaining elements
    for i in range(ai, len(a)):
        merged.append(a[i])
    for i in range(bi, len(b)):
        merged.append(b[i])

    return merged


def mergesort(l: list):
    mid = len(l) // 2

    # split in half
    a = l[:mid]
    b = l[mid:]
    if len(l) <= 2:
        return merge(a, b)

    # recursively merge two split arrays
    return merge(mergesort(a), mergesort(b))


c = [2, 4, 1, 6, 8, 5, 7, 7, 3, 7, 0, -1, -1,1,2,11,32]
print(mergesort(c))
