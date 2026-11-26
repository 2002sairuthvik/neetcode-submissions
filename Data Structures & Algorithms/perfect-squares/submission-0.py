class Solution:
    def numSquares(self, n: int) -> int:
        squares=[]
        k=1
        while k*k<=n:
            squares.append(k*k)
            k+=1
        
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for total in range(n+1):
            for sq in squares:
                if sq>total:
                    break
                dp[total]=min(dp[total],1+dp[total-sq])
        
        return dp[n]