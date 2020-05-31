from PekingUniversity.linear_data_structure import adt_deque


def palcheker(string):
    char_deque = adt_deque.Deque()
    for char in string:
        char_deque.add_rear(char)
    still_equal = True
    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            still_equal = False
    return still_equal
