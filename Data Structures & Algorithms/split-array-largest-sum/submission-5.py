class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r=max(nums),sum(nums)
        res=r
        def canSplit(maxSum):
            sub_array_needed=1
            curr_sum=0
            for num in nums:
                if curr_sum+num > maxSum:
                    sub_array_needed+=1
                    curr_sum=0
                curr_sum+=num
            return sub_array_needed<=k
        while l<=r:
            m=(l+r)//2
            if canSplit(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res