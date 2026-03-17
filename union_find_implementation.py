class UnionFind:
    def __init__ (self , x):
        self.parent[x] = (i for i in range (x))
    def find(self , x):
        