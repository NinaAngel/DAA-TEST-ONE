def insertionSort(A, n):
    for pos in range(1, n):
        nextpos = pos
        while nextpos > 0 and A[nextpos] < A[nextpos - 1]:
            
            A[nextpos], A[nextpos - 1] = A[nextpos - 1], A[nextpos]
            nextpos = nextpos - 1
    return A
