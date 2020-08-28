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



