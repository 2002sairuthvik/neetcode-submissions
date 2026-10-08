class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")]*n
        prices[src]=0

        for i in range(k+1):
            tmpP = prices.copy()
            updated=False
            for s,d,p in flights:
                if prices[s]== float("inf"):
                    continue
                if prices[s]+p < tmpP[d]:
                    tmpP[d] = prices[s]+p
                    updated=True
            prices=tmpP
            if not updated:
                break
        
        return -1 if prices[dst] == float("inf") else prices[dst]