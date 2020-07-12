from .node import Node


class Deque(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        self.items.pop()

    def remove_rear(self):
        self.items.pop(0)


class LinkListDeque(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.previous_tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def get_previous_tail(self, current_tail):
        self.previous_tail = current_tail

    def add_front(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            temp.set_next(self.head)
            self.head = temp
        self.length += 1

    def add_rear(self, item):
        temp = Node(item)
        if self.tail is None:
            self.tail = temp
            self.head = temp
        else:
            self.previous_tail =self.tail
            self.tail.set_next(temp)
            self.tail = self.tail.get_next()
        self.length += 1

    def remove_front(self):
        item = self.head.get_data()
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.get_next()
        self.length -= 1
        return item

    def remove_rear(self):
        item = self.tail.get_data()
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.previous_tail
            self.tail.set_next()
        self.length -= 1
        return item
