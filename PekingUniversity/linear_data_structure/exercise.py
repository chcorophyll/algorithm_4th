import random
from .stack import Stack
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


#  rand hot potato
def random_hot_potato(name_list):
    name_queue = Queue
    for name in name_list:
        name_queue.enqueue(name)
    while name_queue.size() != 1:
        num = random.randint(1, name_queue.size())
        for i in range(num):
            temp = name_queue.dequeue()
            name_queue.enqueue(temp)
        name_queue.dequeue()
    return name_queue.dequeue()

# radix_sort
def radix_sort(s):
    main = Queue()
    for n in s:
        main.enqueue(n)
    d = len(str(max(s)))
    dstr = "%%0%dd" % d
    nums = [Queue() for _ in range(10)]
    for i in range(-1, -d-1, -1):
        while not main.is_empty():
            n = main.dequeue()
            dn = (dstr % n)[i]
            nums[int(dn)].enqueue(n)
        for k in range(10):
            while not nums[k].is_empty():
                main.enqueue(nums[k].dequeue())
    result = []
    while not main.is_empty():
        result.append(main.dequeue())
    print(result)
    return result


# html
def html_match(s):

    def is_open_tag(tag):
        return tag[1] != "/"

    def matches(tag_open, tag_close):
        return tag_open == tag_close.replace("/", "")

    def get_tag(s, i):
        t = ""
        while s[i] != ">":
            t += s[i]
            i += 1
        t += ">"
        return t, i

    st = Stack()
    balanced = True
    index = 0
    while index < len(s) and balanced:
        symbol = s[index]
        if symbol == "<":
            tag, index = get_tag(s, index)
        if is_open_tag(tag):
            st.push(tag)
        else:
            if st.is_empty():
                balanced = False
            else:
                top = st.pop()
                if not matches(top, tag):
                    balanced = False

        while index < len(s) and s[index] != "<":
            index += 1
    if balanced and st.is_empty():
        return True
    else:
        return False

class Node(object):

    def __init__(self, init_data):
        self.data = init_data
        self.previous = None
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next=None):
        self.next = new_next

    def set_previous(self, new_previous):
        self.previous = new_previous

class DoubleLinkedList(object):

    def __init__(self, it=None):
        self.head = None
        self.tail = None
        self.length = 0
        if it is not None:
            for d in it:
                self.append(d)

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.length

    __len__ = size

    def get_tail(self):
        return self.tail

    def add(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.head.set_previous(temp)
            temp.set_next(self.head)
            self.head = temp
        self.length += 1

    def append(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.set_next(temp)
            temp.set_previous(self.tail)
            self.tail = temp
        self.length += 1

    def insert(self, index, item):
        current, current_index = self.head, 0
        while current_index < index:
            current = self.head.get_next()
            current_index += 1
        if current is None:
            if self.head is None:
                self.add(item)
            else:
                self.append(item)
        else:
            temp = Node(item)
            temp.set_previous(current.get_previous())
            temp.set_next(current)
            if temp.get_previous() is not None:
                temp.get_previous().set_next(temp)
            current.set_previous(temp)
        self.length += 1

    def index(self, item):
        current, current_index = self.head, 0
        while current is not None:
            if current.get_data() != item:
                break
            current = self.head.get_next()
            current_index += 1
        else:
            return None
        return current_index

    def search(self, item):
        return self.index(item) is not None

    def delete(self, current):
        if self.head == current:
            self.head = current.get_next()
        if self.tail == current:
            self.tail = current.get_previous()
        if current.get_previous() is not None:
            current.get_previous().set_next(current.get_next())
        if current.get_next() is not None:
            current.get_next().set_previous(current.get_previous())
        self.length -= 1

    def remove(self, item):
        current = self.head
        while current is not None:
            if current.get_data() == item:
                self.delete(current)
                break
            current = current.get_next()

    def pop(self, n=None):
        if n is None:
            n = self.length - 1
        current, i = self.head, 0
        while i < n:
            current = current.get_next()
            i += 1
        item = current.get_data()
        self.delete(current)
        return item

    def __str__(self):
        item_list = []
        current = self.head
        while current is not None:
            item_list.append(current.get_data())
            current = current.get_next()
        return str(item_list)

    __repr__ = __str__

    def __getitem__(self, key):
        if isinstance(key, int):
            current, i = self.head, 0
            while i < key:
                current = current.get_next()
                i += 1
            if current is not None:
                return current.get_data()
            else:
                raise StopAsyncIteration
        elif isinstance(key, slice):
            if key.start is None:
                start = 0
            else:
                start = key.start
            if key.stop is None:
                stop = self.length
            else:
                stop = key.stop
            if key.step is None:
                step = 1
            else:
                step = key.step
            current, i = self.head, 0
            while i < start:
                current = current.get_next()
                i += 1
            data_copy = DoubleLinkedList()
            while i < stop:
                data_copy.append(current.get_data())
                s = step
                while current is not None and s > 0:
                    current = current.get_next()
                    s -= 1
                i += step
            return data_copy

    def __eq__(self, other):
        if other is None or not isinstance(other, DoubleLinkedList):
            return False
        if len(self) != len(other):
            return False
        for s, o in zip(self, other):
            if s != o:
                return False
        else:
            return True

if __name__ == "__main__":
    test_list = [334, 5, 67, 345, 7, 345345,
                 99, 4, 23, 78, 45, 1, 3453,
                 23424]
    radix_sort(test_list)

    from collections import deque
