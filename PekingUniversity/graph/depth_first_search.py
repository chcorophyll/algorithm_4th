from .breadth_first_search import Graph, Vertex


def knight_graph(bd_size):
    knight_tour_graph = Graph()
    for row in range(bd_size):
        for col in range(bd_size):
            node_id = pos_to_node_id(row, col, bd_size)
            new_position = gen_legal_moves(row, col, bd_size)
            for e in new_position:
                new_node_id = pos_to_node_id(e[0], e[1], bd_size)
                knight_tour_graph.add_edge(node_id, new_node_id)
    return knight_tour_graph


def pos_to_node_id(row, col, board_size):
    return row * board_size + col


def gen_legal_moves(row, col, board_size):
    new_moves = []
    moves_offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moves_offsets:
        new_row = row + i[0]
        new_col = col + i[1]
        if legal_coord(new_row, board_size) and legal_coord(new_col, board_size):
            new_moves.append((new_row, new_col))
    return new_moves


def legal_coord(x, board_size):
    if 0 <= x < board_size:
        return True
    else:
        return False


def knight_tour(n, path, u, limit):
    u.set_color("gray")
    path.append(u)
    if n < limit:
        neighbor_list = list(u.get_connections())
        i = 0
        done = False
        while i < len(neighbor_list) and not done:
            if neighbor_list[i].get_color() == "white":
                done = knight_tour(n+1, path, neighbor_list[i], limit)
            i += 1
        if not done:
            path.pop()
            u.set_color("white")
    else:
        done = True
    return done


def order_by_avail(n):
    residual_list = []
    for v in n.get_connections():
        if v.get_color == "white":
            count = 0
            for w in v.get_connections():
                if w.get_color == "white":
                    count += 1
            residual_list.append((c, v))
    residual_list.sort(key=lambda x: x[0])
    return [y[1] for y in residual_list]


def knight_tour_order(n, path, u, limit):
    u.set_color("gray")
    path.append(u)
    if n < limit:
        neighbor_list = order_by_avail(n)
        i = 0
        done = False
        while i < len(neighbor_list) and not done:
            if neighbor_list[i].get_color() == "white":
                done = knight_tour(n+1, path, neighbor_list[i], limit)
            i += 1
        if not done:
            path.pop()
            u.set_color("white")
    else:
        done = True
    return done


class DFSGraph(Graph):

    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for vertex in self:
            vertex.set_color("white")
            vertex.set_pred(-1)
        for vertex in self:
            if vertex.get_color() == "white":
                self.dfs_visit(vertex)

    def dfs_visit(self, start_vertex):
        start_vertex.set_color("gray")
        self.time += 1
        start_vertex.set_discovery(self.time)
        for next_vertex in start_vertex.get_connections():
            if next_vertex.get_color() == "white":
                next_vertex.set_pred(start_vertex)
                self.dfs_visit(next_vertex)
        start_vertex.set_color("black")
        self.time += 1
        start_vertex.set_finish(self.time)
