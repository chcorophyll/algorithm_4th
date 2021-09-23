from .node import Node


class UnorderedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        if self.head == None:
            self.tail = temp
            self.head = temp
        else:
            temp.set_next(self.head)
            self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    # slow version
    # def append(self, item):
    #     current = self.head
    #     previous = None
    #     while current != None:
    #         previous = current
    #         current = current.get_next()
    #     temp = Node(item)
    #     if previous == None:
    #         temp.set_next(current)
    #         self.head = temp
    #     else:
    #         temp.set_next(current)
    #         previous.set_next(temp)

    # fast version
    def append(self, item):
        current = self.tail
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            current.set_next(temp)
            self.tail = temp

    def insert(self, item, index):
        count = 0
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if count == index:
                stop = True
            else:
                count += 1
                previous = current
                current = current.get_next()
        temp = Node(item)
        if previous == None:
            temp.get_next(current)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def index(self, item):
        count = 0
        current = self.head
        stop = False
        while current != None and not stop:
            if current.get_data() == item:
                stop = True
            else:
                count += 1
                current = current.get_next()
        return count

    def pop(self, index=0):
        count = 0
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if count == index:
                stop = True
            else:
                count += 1
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.next())
