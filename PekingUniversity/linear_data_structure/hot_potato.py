from PekingUniversity.linear_data_structure import queue


def hot_potato(name_list, num):
    name_queue = queue.Queue()
    for name in name_list:
        name_queue.enqueue(name)
    while name_queue.size() > 1:
        for i in range(num):
            name_queue.enqueue(name_queue.pop())
        name_queue.dequeue()
    return name_queue.dequeue()
