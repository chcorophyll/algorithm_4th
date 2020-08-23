# version list

# class BinaryTree(object):
#
#     def __init__(self, r):
#         self.tree = [r, [], []]
#
#     def insert_left(self, root, new_branch):
#         t = root.pop(1)
#         if len(t) > 1:
#             root.insert(1, [new_branch, t, []])
#         else:
#             root.tree.insert(1, [new_branch, [], []])
#         return root
#
#     def insert_right(self, root, new_branch):
#         t = root.pop(2)
#         if len(t) > 1:
#             root.insert(2, [new_branch, [], t])
#         else:
#             root.insert(2, [new_branch, [], []])
#         return root
#
#     def get_root(self, root):
#         return root[0]

    # def set_root(self, root, val):
    #     root[0] = val
    #
    # def get_left_child(self, root):
    #     return root[1]
    #
    # def get_right_child(self, root):
    #     return root[2]
    #
    # def build_tree(self, root):
    #     if len(root) < 2:
    #         print("Key:", root[0])
    #     else:
    #         print("Key:", root[0])
    #         print("Left Child:", self.build_tree(root[1]))
    #         print("Right Child:", self.build_tree(root[2]))


class BinaryTree(object):

    def __init__(self, val):
        self.key = val
        self.left_child = None
        self.right_child = None

    def insert_left_tree(self, val):
        if self.left_child is None:
            self.left_child = BinaryTree(val)
        else:
            temp = BinaryTree(val)
            temp.left_child = self.left_child
            self.left_child = temp

    def insert_right_tree(self, val):
        if self.right_child is None:
            self.right_child = BinaryTree(val)
        else:
            temp = BinaryTree(val)
            temp.right_child = self.right_child
            self.right_child = temp

    def get_root(self):
        return self.key

    def set_root(self, val):
        self.key = val

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def build_tree(self):
        if self.left_child:
            self.left_child.build_tree()
        print(self.key)
        if self.right_child:
            self.right_child.build.tree()

