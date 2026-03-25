#union by rank

class UnionFind:
    def __init__ (self , x):
        self.parent[x] = (i for i in range (x))
        self.rank = [0]*x
    def find(self , x):
        while(self.parent[x]!=x):
            x=self.parent[x]
        return x
    def union(self , x ,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x==root_y:
            return
        if self.rank[root_x]<self.rank[root_y]:
            self.parent[root_x]=root_y
        elif self.rank[root_x]>self.rank[root_y]:
            self.parent[root_y]=root_x
        else:
            self.parent[root_y]=root_x
            self.rank[root_x]+=1


#union by size

class UnionFind:
    def __init__ (self , x):
        self.parent[x] = (i for i in range (x))
        self.size = [1]*x
    def find(self , x):
        while(self.parent[x]!=x):
            
            x=self.parent[x]
        return x
    def union(self , x ,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x==root_y:
            return
        if self.rank[root_x]<self.rank[root_y]:
            self.parent[root_x]=root_y
            self.size[root_y]+=self.size[root_x]
        elif self.rank[root_x]>self.rank[root_y]:
            self.parent[root_y]=root_x
            self.size[root_x]+=self.size[root_y]
        else:
            self.parent[root_y]=root_x
            self.size[root_x]+= self.size[root_y]



#union find with path compression

class UnionFind:
    def __init__ (self , x):
        self.parent[x] = (i for i in range (x))
        self.size = [1]*x
    def find(self , x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return x
    def union(self , x ,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x==root_y:
            return
        if self.rank[root_x]<self.rank[root_y]:
            self.parent[root_x]=root_y
            self.size[root_y]+=self.size[root_x]

        elif self.rank[root_x]>self.rank[root_y]:
            self.parent[root_y]=root_x
            self.size[root_x]+=self.size[root_y]

        else:
            self.parent[root_y]=root_x
            self.size[root_x]+= self.size[root_y]
