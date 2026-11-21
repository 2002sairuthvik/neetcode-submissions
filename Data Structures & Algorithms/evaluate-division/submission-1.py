class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent={}
        weight={}

        def find(x):
            if parent[x]!=x:
                orig_parent=parent[x]
                parent[x]=find(orig_parent)
                weight[x]*=weight[orig_parent]
            return parent[x]
        
        def union(a,b,val):
            for node in (a,b):
                if node not in parent:
                    parent[node]=node
                    weight[node]=1.0
            
            ra,rb=find(a),find(b)
            if ra!=rb:
                parent[ra]=rb
                weight[ra]=val*(weight[b]/weight[a])
        for (a,b),val in zip(equations,values):
            union(a,b,val)
        
        res=[]
        for c,d in queries:
            if c not in parent or d not in parent or find(c)!=find(d):
                res.append(-1.0)
            else:
                res.append(weight[c]/weight[d])
        return res

        