from . import priority_queue
from .breadth_first_search import Graph, Vertex


def dijkstra(a_graph, start):
    pq = priority_queue.PriorityQueue()
    start.set_distance(0)
    pq.build_heap([(v.get_distance(), v) for v in a_graph])
    while not pq.is_empty():
        current_vertex = pq.del_min()
        for next_vertex in current_vertex.get_connections():
            new_distance = current_vertex.get_distance() + current_vertex.get_weight(next_vertex)
            if new_distance < next_vertex.get_distance():
                next_vertex.set_distance(new_distance)
                next_vertex.ser_pred(current_vertex)
                pq.decrease_key(next_vertex, new_distance)