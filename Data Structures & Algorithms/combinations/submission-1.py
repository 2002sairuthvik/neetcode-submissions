class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        comb=[]

        def dfs(i,rem):
            if rem==0:
                return res.append(comb.copy())
            
            if i>n or n-i+1<rem:
                return
            
            #include
            comb.append(i)
            dfs(i+1,rem-1)
            comb.pop()

            #exlcude
            dfs(i+1,rem)

        dfs(1,k)
        return res