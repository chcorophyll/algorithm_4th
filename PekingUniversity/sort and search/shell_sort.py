def shell_sort(a_list):
    gap = len(a_list) // 2
    while gap > 0:
        for i in range(gap, len(a_list)):
            current = a_list[i]
            pos_index = i
            while pos_index >= 0 and pos_index - gap >= 0 and a_list[pos_index - gap] > current:
                a_list[pos_index] = a_list[pos_index - gap]
                pos_index -= gap
            a_list[pos_index] = current
        gap = gap // 2


# def shell_sort(list):
#     n = len(list)
#     # 初始步長
#     gap = n // 2
#     while gap > 0:
#         for i in range(gap, n):
#             # 每个步長進行插入排序
#             temp = list[i]
#             j = i
#             # 插入排序
#             while j >= 0 and j-gap >= 0 and list[j - gap] > temp:
#                 list[j] = list[j - gap]
#                 j -= gap
#             list[j] = temp
#         # 得到新的步長
#         gap = gap // 2
#     return list


a_list = [4, 2, 5, 1, 3, 6]
shell_sort(a_list)
print(a_list)