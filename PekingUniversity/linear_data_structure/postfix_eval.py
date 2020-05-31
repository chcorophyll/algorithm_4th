from PekingUniversity.linear_data_structure import stack


def do_math(op, op_1, op_2):
    if op == "*":
        return op_1 * op_2
    elif op == "/":
        return op_2 / op_1
    elif op == "+":
        return op_1 + op_2
    else:
        return op_2 - op_1
    
def postfix_eval(postfix_expr):
    op_stack = stack.Stack()
    token_list = postfix_expr.split()
    for token in token_list:
        if token in "0123456789":
            op_stack.push(int(token))
        else:
            op_first = op_stack.pop()
            op_second = op_stack.pop()
            result = do_math(token, op_first, op_second)
            op_stack.push(result)
    return op_stack.pop()
