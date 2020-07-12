# from .node import Node


class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


class LinklistQueue(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.length

    def enqueue(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.set_next(temp)
            self.tail = self.tail.get_next()
        self.length += 1

    def dequeue(self):
        item = self.head.get_data()
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
        self.length -= 1
        return item

    def peek(self):
        return self.tail.get_data()



class Node(object):

    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.previous = Node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def set_previous(self, new_previous):
        self.previous = new_previous


#  quick
class QuickQueue(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def is_empty(self):
        return self.head == None

    def enqueue(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            temp.set_next(self.head)
            self.head.set_previous(temp)
            self.head = temp

    def dequeue(self):
        item = self.tail.get_data()
        previous = self.tail.get_previous()
        previous.set_next(None)
        self.tail = previous
        return item


