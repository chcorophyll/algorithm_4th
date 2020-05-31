from PekingUniversity.linear_data_structure import stack


def par_checker(symbol_string):
    s = stack.Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False

def matches(opener, closer):
    openers = "([{"
    closers = ")]}"
    return openers.index(opener) == closers.index(closer)

def par_checker(symbol_string):
    s = stack.Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False
