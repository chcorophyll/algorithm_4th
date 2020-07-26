def sequential_search(test_list, item):
    pos = 0
    found = False
    while pos < len(test_list) and not found:
        if test_list[pos] == item:
            found = True
        else:
            pos += 1
    return found


def ordered_sequential_search(ordered_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(ordered_list) and not found and not stop:
        if ordered_list[pos] == item:
            found = True
        else:
            if ordered_list[pos] > item:
                stop = True
            else:
                pos += 1
    return found
