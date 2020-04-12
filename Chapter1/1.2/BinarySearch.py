from Merge_sort import merge_sort


# loop version
def binary_search(arr, val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if val < arr[mid]:
            high = mid - 1
        elif val > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1

# recursive version
def binary_search_recursive(arr, low, high, val):
    if low > high:
        return -1
    mid = (low + high) // 2
    if val < arr[mid]:
        high = mid - 1
        return binary_search_recursive(arr, low, high, val)
    elif val > arr[mid]:
        low = mid + 1
        return binary_search_recursive(arr, low, high, val)
    else:
        return mid


if __name__ == "__main__":
    arr_test = [4, 5, 3, 6, 7, 1, 2]
    arr = merge_sort(arr_test)
    print(arr)
    index = binary_search(arr, 6)
    print(index)
    index = binary_search_recursive(arr, 0, len(arr)-1, 6)
    print(index)
