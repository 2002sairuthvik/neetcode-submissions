class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)% groupSize !=0:
            return False
        count = Counter(hand)
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            if count[first]==0:
                heapq.heappop(minHeap)
                continue 
            for i in range(groupSize):
                card = first+i
                if count[card]==0:
                    return False
                count[card]-=1
        return True
