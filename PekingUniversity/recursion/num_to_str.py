from ..linear_data_structure import stack


def num_to_str(num, base):
    base_str = "0123456789ABCDEF"
    if num < base:
        return base_str[num]
    else:
        return num_to_str(num // base, base) + base_str[num % base]

def reverse_str(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + reverse_str(string[:-1])

def anagram(string):
    string = string.lower()
    string = "".join(s for s in string if s.isalnum())
    if len(string) <= 2:
        return True
    if string[0] != string[-1]:
        return False
    else:
        return anagram(string[1:-1])

str_stack = stack.Stack()
def to_str(num, base):
    base_str = "0123456789ABCDEF"
    while num > 0:
        if num < base:
            str_stack.push(base_str[num])
        else:
            str_stack.push(base_str[num % base])
        num = num // base
    res = ""
    while not str_stack.is_empty():
        res = res + str(str_stack.pop())
    return res

