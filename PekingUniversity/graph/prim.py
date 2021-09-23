import sys
from .priority_queue import PriorityQueue
from .breadth_first_search import Graph, Vertex


def prim(a_graph, start):
    pq = PriorityQueue()
    for vertex in a_graph:
        vertex.set_distance(sys.maxsize)
        vertex.set_pred(None)
    start.set_distance(0)
    pq.build_heap([(v.get_distance(), v) for v in a_graph])
    while not pq.is_empty():
        current_vertex = pq.del_min()
        for next_vertex in current_vertex.get_connections():
            new_cost = current_vertex.get_weight(next_vertex)
            if next_vertex in pq and new_cost < next_vertex.get_distance():
                next_vertex.set_pred(current_vertex)
                next_vertex.set_distance(new_cost)
                pq.decrease_key(next_vertex, new_cost)
