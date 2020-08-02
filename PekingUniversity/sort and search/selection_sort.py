def select_sort(a_list):
    for i in range(len(a_list)-1, 0, -1):
        max_idx = 0
        for j in range(1, i+1):
            if a_list[j] > a_list[max_idx]:
                max_idx = j
        a_list[max_idx], a_list[i] = a_list[i], a_list[max_idx]
