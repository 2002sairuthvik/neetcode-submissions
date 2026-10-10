class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=="0":
            return 0
        
        dp1,dp2=1,1 # represents dp[i+1],dp[i+2]

        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                curr= 0
            else:
                curr=dp1

            if (i+1 <len(s) and(s[i]=="1" or s[i]=="2" and s[i+1] in "0123456")):
                curr+=dp2
            
            dp2=dp1
            dp1=curr

            
        return dp1
        