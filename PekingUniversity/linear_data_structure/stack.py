from .node import Node


class Stack(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class LinkListStack(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.length

    def push(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        self.length += 1

    def pop(self):
        item = self.head.get_data()
        self.head = self.head.get_next()
        self.length -= 1
        return item

    def peek(self):
        return self.head.get_data()
