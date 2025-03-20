def counting_sort(arr):
    """
    계수 정렬을 수행하는 함수
    :param arr: 정렬할 리스트
    :return: 정렬된 리스트
    """
    if len(arr) == 0:
        return arr

    # 배열의 최댓값과 최솟값을 찾아 범위 계산
    max_val = max(arr)
    min_val = min(arr)

    # 계수 배열 생성 (값의 범위가 [min_val, max_val] 범위)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # 각 값에 대한 등장 횟수를 셈
    for num in arr:
        count[num - min_val] += 1

    # 각 계수 배열에 누적 합을 더하여 위치를 계산
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 출력 배열을 작성 (원래 배열의 값을 올바른 위치에 배치)
    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output


if __name__ == '__main__':
    arr = [3, 31, 48, 73, 8, 11, 20, 29, 65, 15]
    print(counting_sort(arr))
