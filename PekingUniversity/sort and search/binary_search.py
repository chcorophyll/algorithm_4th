def binary_search(test_list, item):
    if len(test_list) < 1:
        return False
    first = 0
    last = len(test_list) - 1
    mid = first + (last - first) // 2
    if test_list[mid] == item:
        return True
    elif test_list[mid] > item:
        return binary_search(test_list[0:mid], item)
    elif test_list[mid] < item:
        return binary_search(test_list[mid+1:], item)


a_list = [3, 5, 7, 8, 9]
result = binary_search(a_list, 7)
print(result)

