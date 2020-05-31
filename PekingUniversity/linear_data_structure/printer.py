import random
from PekingUniversity.linear_data_structure import queue


class Printer(object):

    def __init__(self, ppm):
        self.paper_rate = ppm
        self.current_task = None
        self.time_remain = 0

    def tick(self):
        if self.current_task != None:
            self.time_remain -= 1
            if self.time_remain <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remain = new_task.get_page() * 60 / self.paper_rate


class Task(object):

    def __init__(self, time):
        self.time_stamp = time
        self.pages = random.randrange(1, 21)

    def get_stampe(self):
        return self.time_stamp

    def get_page(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.time_stamp


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = queue.Queue()
    waiting_times = []
    for current_time in range(num_seconds):
        if new_print_task():
            task = Task(current_time)
            print_queue.enqueue(task)
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_time))
            lab_printer.start_next(next_task)
        lab_printer.tick()
    average_wait_time = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." %(average_wait_time, print_queue.size()))
