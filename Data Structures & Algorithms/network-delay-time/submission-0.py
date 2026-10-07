class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(n+1)}
        for u,v,t in times:
            adj[u].append((v,t))
        
        minHeap = [(0,k)]
        visited = set()
        totalT = 0

        while minHeap:
            time,u = heapq.heappop(minHeap)
            if u in visited:
                continue
            visited.add(u)
            totalT=time
            if len(visited)==n:
                return totalT
            
            for v,w in adj[u]:
                if v not in visited:
                    heapq.heappush(minHeap,(time+w,v))
        return totalT if len(visited)==n else -1