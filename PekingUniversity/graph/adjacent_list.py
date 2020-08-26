class Vertex(object):

    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight):
        self.connected_to[neighbor] = weight

    def __str__(self):
        return str(self.id) + "connected to:" + str([x.id for x in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connected_to[neighbor]


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