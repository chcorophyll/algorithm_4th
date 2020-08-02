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


def binary_search(test_list, item):
    first = 0
    last = len(test_list) - 1
    found = False
    while first <= last and not found:
        mid = first + (last - first) // 2
        if test_list[mid] == item:
            found = True
        else:
            if test_list[mid] > item:
                last = mid - 1
            else:
                first = mid + 1
    return found

def binary_search(test_list, item):
    if len(test_list) == 0:
        return False
    else:
        mid = len(test_list) // 2
        if test_list[mid] == item:
            return True
        else:
            if test_list[mid] > item:
                return binary_search(test_list[:mid], item)
            else:
                return binary_search(test_list[mid+1:], item)


