class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=defaultdict(list)

        for (a,b),val in zip(equations,values):
            adj[a].append((b,val))
            adj[b].append((a,1.0/val))
        
        def bfs(src,dst):
            if src not in adj or dst not in adj:
                return -1.0
            if src == dst:
                return 1.0
            
            queue=deque([(src,1.0)])
            visited={src}
            while queue:
                curr,prod=queue.popleft()
                if curr==dst:
                    return prod
                
                for nei,weight in adj[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei,weight*prod))
            return -1.0

        return [bfs(b,c) for b,c in queries]
