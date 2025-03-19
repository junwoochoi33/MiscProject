
def merge_sort(arr):

    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2

    left_half = merge_sort(arr[mid:])
    right_half = merge_sort(arr[:mid])

    return merge(left_half, right_half)

def merge(left_half, right_half):

    i = j = 0
    result = []

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    result.extend(left_half[i:])
    result.extend(right_half[j:])

    return result


if __name__ == '__main__':
    print(merge_sort([3, 31, 48, 73, 8, 11, 20, 29, 65, 15]))
