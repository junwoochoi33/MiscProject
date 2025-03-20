
def counting_sort(arr, exp):

    n = len(arr)

    count_arr = [0] * 10
    result_arr = [0] * n

    for i in range(n):
        idx = arr[i] // exp % 10
        count_arr[idx] += 1

    for i in range(1, 10):
        count_arr[i] += count_arr[i-1]

    for i in range(n - 1, -1, -1):
        idx = arr[i] // exp % 10
        count_arr[idx] -= 1
        result_arr[count_arr[idx]] = arr[i]

    return result_arr



def radix_sort(arr):

    max_val = max(arr)

    exp = 1
    while max_val // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10

    return arr


