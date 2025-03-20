def heapify(arr, n, i):
    """
    주어진 인덱스 i를 루트로 하여 최대 힙을 유지하는 함수
    :param arr: 정렬할 리스트
    :param n: 힙의 크기
    :param i: 현재 노드의 인덱스
    """
    largest = i  # 현재 노드의 인덱스를 가장 큰 값으로 설정
    left = 2 * i + 1  # 왼쪽 자식 노드의 인덱스
    right = 2 * i + 2  # 오른쪽 자식 노드의 인덱스

    # 왼쪽 자식이 루트보다 크면 largest를 왼쪽 자식의 인덱스로 설정
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 현재까지 가장 큰 값보다 크면 largest를 오른쪽 자식의 인덱스로 설정
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 만약 largest가 변경되었다면 (즉, 자식이 더 크다면)
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 값 교환
        heapify(arr, n, largest)  # 변경된 위치에서 다시 힙 구조를 유지

def heap_sort(arr):
    """
    힙 정렬을 수행하는 함수
    :param arr: 정렬할 리스트
    :return: 정렬된 리스트
    """
    n = len(arr)

    # 힙을 최대 힙으로 만들기
    for i in range(n // 2 - 1, -1, -1):  # 마지막 비 리프 노드부터 시작
        heapify(arr, n, i)

    # 최대 힙에서 루트(가장 큰 값)을 하나씩 빼고 정렬
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 루트와 마지막 원소 교환
        heapify(arr, i, 0)  # 힙의 크기를 줄이고, 루트부터 다시 힙ify

    return arr

# 예시 실행
arr = [12, 11, 13, 5, 6, 7]
print("정렬된 배열:", heap_sort(arr))
