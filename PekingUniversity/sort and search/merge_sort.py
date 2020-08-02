def merge_sort(a_list):
    # base case
    if len(a_list) <= 1:
        return a_list
    else:
        # sort
        left = 0
        right = len(a_list)
        mid = left + (right - left) // 2
        sort_left = merge_sort(a_list[0:mid])
        sort_right = merge_sort(a_list[mid:])
        # merge
        sort_list = []
        while len(sort_left) != 0 and len(sort_right) != 0:
            if sort_left[0] <= sort_right[0]:
                sort_list.append(sort_left.pop(0))
            else:
                sort_list.append(sort_right.pop(0))
        if sort_left:
            sort_list.extend(sort_left)
        if sort_right:
            sort_list.extend(sort_right)
        return sort_list


a_list = [3, 2, 5, 1, 0, 4]
print(merge_sort(a_list))
