class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l,r=0,len(nums)-1
        while l<r:
            if nums[l]==nums[r]:
                return k == abs(r-l)
            l+=1
            r-=1