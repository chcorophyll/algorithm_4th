def shell_sort(arr):
    n = len(arr)
    gap = 1
    while gap < n / 3:
        gap = 3 * gap + 1
    while gap >= 1:
        print(gap)
        for i in range(gap, n):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j = j - gap
            arr[j + gap] = temp
        gap = gap // 3
    return arr



