from .adjacent_list import Graph


def build_graph(word_file):
    d = {}
    g = Graph()
    with open(word_file, "r") as file:
        for line in file:
            word = line[:-1]
            for i in range(len(word)):
                bucket = word[:i] + "_" + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
    for bucket in d:
        for word_1 in d[bucket]:
            for word_2 in d[bucket]:
                if word_1 != word_2:
                    g.add_edge(word_1, word_2)