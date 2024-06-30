class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # DSU implementation
        class DSU:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [1] * size
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                
                if rootX != rootY:
                    if self.rank[rootX] > self.rank[rootY]:
                        self.parent[rootY] = rootX
                    elif self.rank[rootX] < self.rank[rootY]:
                        self.parent[rootX] = rootY
                    else:
                        self.parent[rootY] = rootX
                        self.rank[rootX] += 1
                    return True
                return False
        
        # Initialize DSU for Alice and Bob
        dsu_alice = DSU(n + 1)
        dsu_bob = DSU(n + 1)
        
        edges_required = 0
        
        # Step 1: Add all type 3 edges
        for type_, u, v in edges:
            if type_ == 3:
                if dsu_alice.union(u, v):
                    dsu_bob.union(u, v)
                    edges_required += 1
        
        # Step 2: Add type 1 edges for Alice and type 2 edges for Bob
        for type_, u, v in edges:
            if type_ == 1:
                if dsu_alice.union(u, v):
                    edges_required += 1
            elif type_ == 2:
                if dsu_bob.union(u, v):
                    edges_required += 1
        
        # Step 3: Check if both Alice and Bob can fully traverse the graph
        if len(set(dsu_alice.find(i) for i in range(1, n + 1))) > 1 or len(set(dsu_bob.find(i) for i in range(1, n + 1))) > 1:
            return -1
        
        # The number of removable edges is the total number of edges minus the required edges
        return len(edges) - edges_required
