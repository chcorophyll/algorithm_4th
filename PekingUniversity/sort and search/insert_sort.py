def insert_sort(a_list):
    for i in range(1, len(a_list)):
        while a_list[i] < a_list[i-1] and i > 0:
            a_list[i], a_list[i-1] = a_list[i-1], a_list[i]
            i -= 1


def insert_sort(a_list):
    for i in range(len(a_list)):
        pre_idx = i - 1
        current = a_list[i]
        while pre_idx >= 0 and a_list[pre_idx] > current:
            a_list[pre_idx+1] = a_list[pre_idx]
            pre_idx -= 1
        a_list[pre_idx+1] = current


a_list = [3, 2, 5, 4, 1, 8]
insert_sort(a_list)
print(a_list)