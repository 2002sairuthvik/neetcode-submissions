class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #building adj list for the given edges and undirected 
        adj = {i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        connections = 0

        #dfs 
        def dfs(i):
            for neighbour in adj[i]:
                if neighbour not in visit:
                    visit.add(neighbour)
                    dfs(neighbour)

        # iterating node by node
        for i in range(n):
            if i not in visit:
                connections+=1
                visit.add(i)
                dfs(i)
        return connections