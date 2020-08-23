class Binary_heap(object):

    def __init__(self):
        self.current_size = 0
        self.heap_list = [0]

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                temp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = temp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    # def perc_down(self, index):
    #     current_index = index
    #     while 2 * current_index <= self.current_size:
    #         if self.heap_list[current_index] > self.heap_list[2*current_index] or self.heap_list[current_index] > self.heap_list[2*current_index+1]:
    #             if self.heap_list[current_index * 2] < self.heap_list[current_index*2 + 1]:
    #                 temp = self.heap_list[current_index]
    #                 self.heap_list[self.current_index] = self.current_size[2*current_index]
    #                 self.heap_list[2*self.current_index] = temp
    #                 current_index = 2 * self.current_index
    #             else:
    #                 temp = self.heap_list[current_index]
    #                 self.heap_list[self.current_index] = self.current_size[2*current_index+1]
    #                 self.heap_list[2*self.current_index+1] = temp
    #                 current_index = 2 * self.current_index + 1

    def perc_down(self, i):
        while (2 * i) <= self.current_size:
            mc = self.min_cnild(i)
            if self.heap_list[i] > self.heap_list[mc]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = temp
            i = mc

    def min_child(self, i):
        if 2 * i + 1 > self.current_size:
            return 2 * i
        else:
            if self.heap_list[2*i] < self.heap_list[2*i+1]:
                return 2 * i
            else:
                return 2 * i + 1

    def del_min(self):
        temp = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return temp

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list
        while i > 0:
            self.perc_down(i)
            i -= 1

