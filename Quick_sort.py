# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = arr[0]
#     low = 0
#     high = len(arr) - 1
#     while low < high:
#         while low < high and arr[high] > mid:
#             high -= 1
#         arr[low] = arr[high]
#         while low < high and arr[low] <= mid:
#             low += 1
#         arr[high] = arr[low]
#     arr[low] = mid
#     arr[0:low] = quick_sort(arr[0:low])
#     arr[low+1:] = quick_sort(arr[low+1:])
#     return arr


def quick_sort(alist, first, last):
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value
    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)


if __name__ == "__main__":
    arr = [3, 2, 4, 1, 5, 7, 0]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)


