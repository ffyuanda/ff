""" self-realized insertion sort python version """
# https://www.youtube.com/watch?v=i-SKeOcBwko


def insertionsort(a: list):
    bound = 1
    while bound < len(a):
        curr, insert = a[bound], 0
        # iterate downward from the boundary between sorted and unsorted (bound)
        for j in range(bound-1, -1, -1):
            if a[j] >= curr:
                # move the cards
                a[j+1] = a[j]
            else:
                # found the insertion index
                insert = j + 1
                break
        a[insert] = curr
        bound += 1
    return a


l = [7, 2, 4, 1, 5, 3]
print(insertionsort(l))
