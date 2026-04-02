class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # make adj AND DO BFS FIND CYCLE 
        adj=[[] for _ in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        q=deque()
        q.append((0,-1))
        vis=set()
        vis.add(0)
        while q:
            curr,parent=q.pop()
            for i in adj[curr]:
                if i ==parent:
                    continue
                if i in vis:
                    return False
                q.append((i,curr))
                vis.add(i)
        if len(vis)!=n:
            return False
        return True