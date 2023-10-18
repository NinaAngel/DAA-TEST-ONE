def insertionSort(A, n):
    for pos in range(1, n):
        nextpos = pos
        while nextpos > 0 and A[nextpos] < A[nextpos - 1]:
            
            A[nextpos], A[nextpos - 1] = A[nextpos - 1], A[nextpos]
            nextpos = nextpos - 1
    return A


unsorted_list = [8, 4, 12, 2, 9, 5, 17, 1, 6, 3]


sorted_list = insertionSort(unsorted_list, len(unsorted_list))


print(sorted_list)
