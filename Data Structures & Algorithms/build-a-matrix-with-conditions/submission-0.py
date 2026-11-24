class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo(conditions):
            adj=defaultdict(list)
            in_degree=[0]*(k+1)

            for u,v in conditions:
                adj[u].append(v)
                in_degree[v]+=1
            
            queue = deque([i for i in range(1,k+1) if in_degree[i]==0])
            order=[]

            while queue:
                curr=queue.popleft()
                order.append(curr)
                for nxt in adj[curr]:
                    in_degree[nxt]-=1
                    if in_degree[nxt]==0:
                        queue.append(nxt)
                
            return order if len(order)==k else []

        
        row_order = topo(rowConditions)
        col_order = topo(colConditions)

        if not row_order or not col_order:
            return []
        
        row_pos = {num:r for num,r in enumerate(row_order)}
        col_pos = {num:c for num,c in enumerate(row_order)}

        matrix=[[0]*k for _ in range(k)]
        for num in range(1,k+1):
            matrix[row_pos[num]][col_pos[num]]=num
        return matrix



        