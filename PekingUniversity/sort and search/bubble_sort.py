def bubble_sort(a_list):
    for i in range(len(a_list) - 1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j+1]:
                a_list[j+1], a_list[j] = a_list[j], a_list[j+1]



def bubble_sort(a_list):
    exchange = True
    i = len(a_list) - 1
    while i > 0 and exchange:
        exchange = False
        for j in range(1):
            if a_list[j] > a_list[j+1]:
                a_list[j + 1], a_list[j] = a_list[j], a_list[j + 1]
                exchange = True
        i -= 1