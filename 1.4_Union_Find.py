class Union_Find:

    def __init__(self, n):
        self.count = n
        self.id = list(range(n))
        self.sz = [1] * n

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    # quick find
    # def find(self, p):
    #     return self.id[p]
    #
    # def union(self, p, q):
    #     p_id = self.find(p)
    #     q_id = self.find(q)
    #     if p_id == q_id:
    #         return
    #     for index, i in enumerate(self.id):
    #         if i == p_id:
    #             self.id[index] = q_id
    #     self.count -= 1

    # quick find-union
    # def find(self, p):
    #     while self.id[p] != p:
    #         p = self.id[p]
    #     return p
    #
    # def union(self, p, q):
    #     p_id = self.find(p)
    #     q_id = self.find(q)
    #     if p_id == q_id:
    #         return
    #     self.id[p_id] = q_id
    #     self.count -= 1

    # weight quick-union
    def find(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return
        if self.sz[p_id] < self.sz[q_id]:
            self.id[p_id] = q_id
            self.sz[q_id] += self.sz[p_id]
        else:
            self.id[q_id] = p_id
            self.sz[p_id] = self.sz[q_id]
        self.count -= 1


if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    uf = Union_Find(n)
    for line in sys.stdin:
        p, q = [int(i) for i in line.split()]
        if (uf.connected(p, q)):
            continue
        else:
            uf.union(p, q)
            print("%s, %s" %(p, q))
    print(uf.count, "component")



