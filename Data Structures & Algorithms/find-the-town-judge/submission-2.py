class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)

        for a,b in trust:
            delta[b]+=1
            delta[a]-=1
        
        if len(delta)==n:
            return -1
        
        for i in range(1,n+1):
            if delta[i]==n-1:
                return i
        return -1