class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        index_tasks = [(enq,proc,idx) for idx,(enq,proc) in enumerate(tasks)]
        index_tasks.sort(key=lambda x:x[0])
        res=[]
        minHeap=[]
        time,i=0,0
        n=len(index_tasks)

        while i<n or minHeap:
            if not minHeap and time<index_tasks[i][0]:
                time=index_tasks[i][0]
            
            while i<n and index_tasks[i][0]<=time:
                heapq.heappush(minHeap,[index_tasks[i][1],index_tasks[i][2]])
                i+=1
            
            proc_time,ord_idx=heapq.heappop(minHeap)
            time+=proc_time
            res.append(ord_idx)
        return res