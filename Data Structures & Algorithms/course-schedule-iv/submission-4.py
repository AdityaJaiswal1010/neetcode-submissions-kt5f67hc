from functools import lru_cache

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            adj[pre[0]].append(pre[1])
        
        adj_tuple = tuple(tuple(x) for x in adj)
        
        res = []
        for query in queries:
            res.append(self.dfs(adj_tuple, query[0], query[1])) 
        return res
    
    @lru_cache(maxsize=None)
    def dfs(self, adj, node, target):
        if node == target:
            return True
        for nei in adj[node]:
            if self.dfs(adj, nei, target):
                return True
        return False