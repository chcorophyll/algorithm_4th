import sys
import os
from ..linear_data_structure import queue

class Vertex(object):

    def __init__(self, num):
        self.id = num
        self.connected_to = {}
        self.color = "white"
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def set_color(self, color):
        self.color = color

    def set_distance(self, d):
        self.dist = d

    def set_pred(self, p):
        self.pred = p

    def set_discovery(self, d_time):
        self.disc = d_time

    def set_finish(self, f_time):
        self.fin = f_time

    def get_finish(self):
        return self.fin

    def get_discovery(self):
        return self.disc

    def get_pred(self):
        return self.pred

    def get_distance(self):
        return self.dist

    def get_color(self):
        return self.color

    def get_connections(self):
        return self.connected_to.keys()

    def get_weight(self, neighbor):
        return self.connected_to[neighbor]

    def __str__(self):
        return str(self.id) + ":color" + self.color + ":disc" + str(self.disc) + ":fin" + str(self.fin) + ":dist" + str(self.dist) + ":pred \n\t[" + str(self.pred) + "]\n"

    def get_id(self):
        return self.id


class Graph(object):

    def __init__(self):
        self.vertex_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertex_list:
            return self.vertex_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertex_list

    def add_edge(self, from_vertex, to_vertex, cost=0):
        if from_vertex not in self.vertex_list:
            new_vertex = self.add_vertex(from_vertex)
        if to_vertex not in self.vertex_list:
            new_vertex = self.add_vertex(to_vertex)
            self.vertex_list[from_vertex].add_neighbor(self.vertex_list[to_vertex], cost)

    def get_vertices(self):
        return self.vertex_list.keys()

    def __iter__(self):
        return iter(self.vertex_list.values())


def breadth_first_search(g, start):
    start.set_distance(0)
    start.set_pred(None)
    vertex_queue = queue.Queue()
    vertex_queue.enqueue(start)
    while vertex_queue.size() > 0:
        current_vertex = vertex_queue.dequeue()
        for neighbor in current_vertex.get_connections():
            if neighbor.get_color() == "white":
                neighbor.set_color("gray")
                neighbor.set_distance(current_vertex.get_distance() + 1)
                neighbor.set_pred(current_vertex)
                vertex_queue.enqueue(neighbor)


def traverse(y):
    x = y
    while x.get_pred():
        print(x.get_id())
        x = x.get_pred()
    print(x.get_id)
