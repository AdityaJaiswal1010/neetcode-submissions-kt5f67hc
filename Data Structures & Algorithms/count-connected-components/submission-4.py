class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        visited = [0] * n
        adj = [[] for _ in range(n)]
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        for i in range(n):
            if visited[i] == 0:
                ans += 1
                self.dfs(adj, i, visited)
        
        return ans
    
    def dfs(self, adj, i, visited):
        visited[i] = 1
        for j in adj[i]:
            if visited[j] == 0:
                self.dfs(adj, j, visited)