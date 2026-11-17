class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n=len(profits)

        projects=sorted(zip(capital,profits))

        max_profit=[]
        i=0

        for _ in range(min(n,k)):
            while i<n and projects[i][0]<=w:
                heapq.heappush(max_profit,-1*projects[i][-1])
                i+=1
            
            if not max_profit:
                break
            
            w+= -heapq.heappop(max_profit)
        return w