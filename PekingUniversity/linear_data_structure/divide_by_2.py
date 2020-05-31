from PekingUniversity.linear_data_structure import stack


def divide_by_2(dec_number):
    remstack = stack.Stack()

    while dec_number > 0:
        rem = dec_number % 2
        remstack.push(rem)
        dec_number = dec_number // 2

    bin_string = ""
    while not remstack.is_empty():
        bin_string = bin_string + str(remstack.pop())

    return bin_string

def base_conventor(dec_number, base):
    digits = "0123456789ABCDEF"
    remstack = stack.Stack()

    while dec_number > 0:
        rem = dec_number % base
        remstack.push(rem)
        dec_number = dec_number // base

    base_string = ""

    while not remstack.is_empty():
        base_string = base_string + digits[remstack.pop()]

    return base_string
