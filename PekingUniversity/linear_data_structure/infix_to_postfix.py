from PekingUniversity.linear_data_structure import stack


def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = stack.Stack()
    post_fix_list = []
    token_list = infix_expr.split()
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            post_fix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                post_fix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                post_fix_list.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.is_empty():
        post_fix_list.append(op_stack.pop())
    return " ".join(post_fix_list)
