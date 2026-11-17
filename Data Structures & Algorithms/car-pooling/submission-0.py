class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x : x[1])
        minHeap=[]
        curPass=0

        for passengers,start,end in trips:
            while minHeap and minHeap[0][0]<=start:
                _,dropped = heapq.heappop(minHeap)
                curPass-=dropped
            
            curPass+=passengers
            if curPass>capacity:
                return False
            
            heapq.heappush(minHeap,(end,passengers))
        return True