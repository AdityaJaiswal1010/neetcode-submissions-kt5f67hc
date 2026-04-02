class Solution:
    def __init__(self):
        self.adj = []
        self.cycle = []
    
    def dfs(self, curr, prev, vis, nodeToIndex, path, found):
        if found[0]:
            return
        
        # cycle found
        if nodeToIndex.get(curr, -1) >= 0:
            startIdx = nodeToIndex[curr]
            for i in range(startIdx, len(path)):
                self.cycle.append(path[i])
            self.cycle.append(curr)
            found[0] = True
            return
        
        vis[curr] = 1
        nodeToIndex[curr] = len(path)
        path.append(curr)
        
        for nei in self.adj[curr]:
            if nei == prev:
                continue
            if found[0]:
                return
            self.dfs(nei, curr, vis, nodeToIndex, path, found)
        
        path.pop()
        del nodeToIndex[curr]
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.adj = [[] for _ in range(n + 1)]
        self.cycle = []
        
        for e in edges:
            self.adj[e[0]].append(e[1])
            self.adj[e[1]].append(e[0])
        
        vis = [0] * (n + 1)
        nodeToIndex = {}
        path = []
        found = [False]      # list so dfs can modify it
        
        for i in range(1, n + 1):
            if self.adj[i] and not vis[i]:
                self.dfs(i, -1, vis, nodeToIndex, path, found)
                if found[0]:
                    break
        
        a, b = 0, 0
        circularPath = set(self.cycle)
        
        for i in range(len(edges)):
            if edges[i][0] in circularPath and edges[i][1] in circularPath:
                a = edges[i][0]
                b = edges[i][1]
        
        return [a, b]