import operator
from ..linear_data_structure import stack
from .binary_tree import BinaryTree


class ParseTree(object):

    def __init__(self, fp_exp):
        self.fp_list = fp_exp.split()
        self.parent_stack = stack.Stack()

    def build_tree(self):
        empty_tree = BinaryTree("")
        self.parent_stack.push(empty_tree)
        current_tree = empty_tree
        for i in self.fp_list:
            if i == "(":
                current_tree.insert_left_tree("")
                self.parent_stack.push(current_tree)
                current_tree = current_tree.get_left_child()
            elif i not in ["+", "-", "*", "/", ")"]:
                current_tree.set_root(i)
                parent_tree = self.parent_stack.pop()
                current_tree = parent_tree
            elif i in ["+", "-", "*", "/"]:
                current_tree.set_root(i)
                current_tree.insert_right_tree("")
                self.parent_stack.push(current_tree)
                current_tree = current_tree.get_right_child()
            elif i == ")":
                current_tree = self.parent_stack.pop()
            else:
                raise ValueError
        return empty_tree

    def evaluate(self, parse_tree):
        operations = {"+": operator.add(), "-": operator.sub(), "*": operator.mul(), "/": operator.truediv()}
        left_child = parse_tree.get_left_child()
        right_child = parse_tree.get_right_child()
        if left_child and right_child:
            operation = operations[parse_tree.get_root()]
            return operation(self.evaluate(left_child), self.evaluate(right_child))
        else:
            return parse_tree.get_root()

    def post_order_evaluate(self, parse_tree):
        operations = {"+": operator.add(), "-": operator.sub(), "*": operator.mul(), "/": operator.truediv()}
        left_result = None
        right_result = None
        if parse_tree:
            left_result = self.post_order_evaluate(parse_tree.get_left_child())
            right_result = self.post_order_evaluate(parse_tree.get_right_child())
            if left_result and right_result:
                return operations[parse_tree.get_root()](left_result, right_result)
            else:
                return parse_tree.get_root()

    def pre_order(self, tree):
        if tree:
            print(tree.get_root)
            if tree.get_left_child():
                self.pre_order(tree.get_left_child())
            if tree.get_right_child():
                self.pre_order(tree.get_right_child())

    def post_order(self, tree):
        if tree:
            if tree.get_left_child():
                self.post_order(tree.get_left_child())
            if tree.get_right_child():
                self.post_order(tree.get_right_child())
            print(tree.get_root)

    def in_order(self, tree):
        if tree:
            if tree.get_left_child():
                self.pre_order(tree.get_left_child())
            print(tree.get_root)
            if tree.get_right_child():
                self.pre_order(tree.get_right_child())

    def print_expression(self, parse_tree):
        string_val = ""
        if parse_tree:
            string_val = "(" + self.print_expression(parse_tree.get_left_child())
            string_val += parse_tree.get_root()
            string_val = string_val + self.print_expression(parse_tree.get_right_child()) + ")"
        return string_val


