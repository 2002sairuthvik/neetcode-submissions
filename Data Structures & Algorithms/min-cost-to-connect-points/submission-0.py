class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visit = set()
        minHeap = [(0,0)]
        totalcost=0

        while len(visit)<n:
            cost,u = heapq.heappop(minHeap)
            if u in visit:
                continue
            
            visit.add(u)
            totalcost+=cost
            x1,y1 = points[u]
            for v in range(n):
                if v not in visit:
                    dist = abs(x1-points[v][0])+abs(y1-points[v][1])
                    heapq.heappush(minHeap,(dist,v))
                
        return totalcost