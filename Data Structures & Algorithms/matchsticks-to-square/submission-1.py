class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks)<4:
            return False
        total=sum(matchsticks)
        if total%4 != 0:
            return False
        
        target = total//4
        matchsticks.sort(reverse=True)

        if matchsticks[0]>target:
            return False
        
        sides=[0]*4
        def backtrack(i):
            if i == len(matchsticks):
                return True
            seen=set()
            for j in range(4):
                if sides[j]+matchsticks[i]>target or sides[j] in seen:
                    continue
                seen.add(sides[j])
                sides[j]+=matchsticks[i]

                if backtrack(i+1):
                    return True
                
                sides[j]-=matchsticks[i]

                if sides[j]==0:
                    return False
            return False
        return backtrack(0)