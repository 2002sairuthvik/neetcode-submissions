import bisect
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        pref=[0]*(n+1)
        for i in range(n):
            pref[i+1]=pref[i]+nums[i]
        
        min_len=float('inf')
        for i in range(n):
            needed=pref[i]+target
            j=bisect.bisect_left(pref,needed)
            if j<=n:
                min_len=min(min_len,j-i)
        return min_len if min_len!=float('inf') else 0