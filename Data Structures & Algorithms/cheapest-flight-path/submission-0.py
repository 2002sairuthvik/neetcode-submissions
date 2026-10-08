class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,p in flights:
            adj[u].append((v,p))
        
        mH = [(0,0,src)] #cost,stops_used,curr_node
        min_stops = {}

        while mH:
            cost,stops,u = heapq.heappop(mH)

            if u==dst:
                return cost
            
            if stops>k:
                continue

            if u in min_stops and stops>=min_stops[u]:
                continue
            
            min_stops[u]=stops

            for v,price in adj[u]:
                heapq.heappush(mH, (cost+price,stops+1,v))
        return -1
