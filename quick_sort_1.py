
def quick_sort_1(arr):

    n = len(arr)

    if n <= 1:
        return arr

    pivot = arr[n-1]
    left_half = [value for value in arr if value < pivot]
    right_half = [value for value in arr if value > pivot]

    return quick_sort_1(left_half) + [pivot] + quick_sort_1(right_half)


