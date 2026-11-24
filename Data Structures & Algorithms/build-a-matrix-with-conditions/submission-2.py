class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src,adj,visit,path,order):
            if src in path:
                return False
            if src in visit:
                return True
            path.add(src)
            visit.add(src)
            for nei in adj[src]:
                if not dfs(nei,adj,visit,path,order):
                    return False
            path.remove(src)
            order.append(src)
            return True
        
        def topo(edges):
            adj=defaultdict(list)
            for src,dst in edges:
                adj[src].append(dst)
            visit,path=set(),set()
            order=[]
            for src in range(1,k+1):
                if not dfs(src,adj,visit,path,order):
                    return []
            return order[::-1]
            
        row_order=topo(rowConditions)
        col_order=topo(colConditions)
        if not row_order or not col_order:
            return []
        
        res=[[0]*k for _ in range(k)]
        row_num = {num:r for r,num in enumerate(row_order)}
        col_num = {num:c for c,num in enumerate(col_order)}

        for num in range(1,k+1):
            res[row_num[num]][col_num[num]]=num
        return res