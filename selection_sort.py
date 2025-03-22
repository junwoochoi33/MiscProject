
def selection_sort(arr):

    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    return arr


