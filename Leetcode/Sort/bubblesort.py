""" self-realized bubble sort python version """
# https://www.youtube.com/watch?v=Jdtq5uKz-w4


def bubblesort(a: list):
    length = len(a)
    for i in range(length):
        flag = 0
        for j in range(length - i - 1):
            # no need to go through the sorted part
            if a[j] >= a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                flag = 1
        if flag == 0:
            # no swap at all: already sorted
            break
    return a


l = [2, 3, 1, 4, 7, 5]
print(bubblesort(l))
