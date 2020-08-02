# def quick_sort(a_list):
#     # base case
#     if len(a_list) <= 1:
#         return a_list
#     else:
#         pivot = a_list[0]
#         index = 1
#         for i in range(1, len(a_list)):
#             if a_list[i] <= pivot:
#                 a_list[index], a_list[i] = a_list[i], a_list[index]
#                 index += 1
#         a_list[index-1], a_list[0] = a_list[0], a_list[index-1]
#         a_list[0:index-1] = quick_sort(a_list[0:index-1])
#         a_list[index:] = quick_sort(a_list[index:])
#     return a_list


def quick_sort(a_list, left, right):
    # base case
    if left > right:
        return
    else:
        pivot = a_list[left]
        low = left + 1
        high = right
        while low <= high:
            while low <= high and a_list[high] >= pivot:
                high -= 1
            while low <= high and a_list[low] < pivot:
                low += 1
            if low <= high:
                a_list[low], a_list[high] = a_list[high], a_list[low]
        a_list[high], a_list[left] = a_list[left], a_list[high]
        quick_sort(a_list, left, high-1)
        quick_sort(a_list, high+1, right)


a_list = [3, 2, 5, 1, 0, 4, 5, 0, 8]
quick_sort(a_list, 0, len(a_list)-1)
print(a_list)
