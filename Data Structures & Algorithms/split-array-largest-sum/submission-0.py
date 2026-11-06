class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        dp={}

        def dfs(i,m):
            if m==1:
                return sum(nums[i:])
            if (i,m) in dp:
                return dp[(i,m)]
            
            res, CurSum=float('inf'),0
            for j in range(i,len(nums)-m+1):
                CurSum+=nums[j]
                maxsum=max(CurSum, dfs(j+1,m-1))
                res = min(res,maxsum)
                if CurSum>res:
                    break
            dp[(i,m)]=res
            return res
        return dfs(0,k)

