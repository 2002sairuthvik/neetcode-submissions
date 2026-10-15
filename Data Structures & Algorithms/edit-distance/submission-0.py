class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
       m , n = len(word1), len(word2)

       # base case when word1 is empty then cost is inserting all char from word2
       dp = [n-j for j in range(n+1)]

       for i in range(m-1,-1,-1):
        new_dp = [0]*(n+1)
        # base case  when word2 is empty then cost is removing all char from word1
        new_dp[n]=m-i
        for j in range(n-1,-1,-1):
            if word1[i]==word2[j]:
                new_dp[j]=dp[j+1]
            else:
                new_dp[j] = 1+min(dp[j+1],dp[j],new_dp[j+1])
        dp = new_dp
       return dp[0]