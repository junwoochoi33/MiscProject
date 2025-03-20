
def heapify(arr, n, i):

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if n > left and arr[left] > arr[largest]: # 주의: arr[left]
        largest = left

    if n > right and arr[right] > arr[largest]: # 주의: arr[right]
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1): # 주의: n // 2 - 1
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr