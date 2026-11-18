class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts=defaultdict(set)
        trusted_by=defaultdict(int)

        for a,b in trust:
            trusts[a].add(b)
            trusted_by[b]+=1
        
        if len(trust)==n:
            return -1
        
        for person in range(1,n+1):
            if person not in trusts and trusted_by[person]==n-1:
                return person
        return -1