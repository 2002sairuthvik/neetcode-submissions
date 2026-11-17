class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap=[]
        for count,ch in [(a,"a"),(b,"b"),(c,"c")]:
            if count >0:
                heapq.heappush(maxHeap,(-count,ch))
        
        res=[]
        while maxHeap:
            neg_cnt1,ch1=heapq.heappop(maxHeap)

            if len(res)>=2 and res[-1]==res[-2]==ch1:
                if not maxHeap:
                    break
                
                neg_cnt2,ch2=heapq.heappop(maxHeap)
                res.append(ch2)
                neg_cnt2+=1
                if neg_cnt2<0:
                    heapq.heappush(maxHeap,(neg_cnt2,ch2))
                
                heapq.heappush(maxHeap,(neg_cnt1,ch1))
            else:
                res.append(ch1)
                neg_cnt1+=1
                if neg_cnt1<0:
                    heapq.heappush(maxHeap,(neg_cnt1,ch1))
        
        return "".join(res)
