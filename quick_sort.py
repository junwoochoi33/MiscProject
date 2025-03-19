
def quick_sort(arr):

    n = len(arr)

    if n <= 1:
        return arr

    pivot = arr[n-1]
    left_half = [value for value in arr if value < pivot]
    right_half = [value for value in arr if value > pivot]

    return quick_sort(left_half) + [pivot] + quick_sort(right_half)



if __name__ == '__main__':
    print(quick_sort([3, 31, 48, 73, 8, 11, 20, 29, 65, 15]))
