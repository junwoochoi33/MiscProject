
def quick_sort_2(arr, low, high):

    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_2(arr, low, pivot_index - 1)
        quick_sort_2(arr, pivot_index + 1, high)
    return arr

def partition(arr, low, high):

    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1




