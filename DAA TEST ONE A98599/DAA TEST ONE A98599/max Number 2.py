Function find_max(arr):
    if arr is empty:
        return None
    max = arr[0]
    for i from 1 to length(arr) - 1:
        if arr[i] > max:
            max = arr[i]
    return max
