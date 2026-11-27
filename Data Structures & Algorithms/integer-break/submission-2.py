class Solution:
    def integerBreak(self, n: int) -> int:
        memo={1:1}
        def dfs(num):
            if num in memo:
                memo[num]
            
            memo[num]=0 if num==n else num
            for i in range(1,(num//2)+1):
                val = dfs(i) * dfs(num-i)
                memo[num]=max(memo[num],val)
            
            return memo[num]
        return dfs(n)
        