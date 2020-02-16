class ResizingArrayStack():

    def __init__(self, item):
        self.num = len(item)
        self.item = item

    def _is_empty(self):
        retrun (self.num == 0)

    def _size(self):
        return self.num

    def resize(self, max_num):
        pass

    def _push(self, push_item):
        self.num += 1
        self.item[self.num] = push_item

    def _pop(self):
        pop_item = self.item[self.num]
        self.num -= 1
