def heaptify(n, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heaptify(n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heaptify(n, i)
    for j in range(n-1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        n -= 1
        heaptify(n, 0)


if __name__ == "__main__":
    arr = [3, 2, 5, 6, 1, 8, 2]
    print(arr)
    heap_sort(arr)
    print("Sorted Arr:", arr)