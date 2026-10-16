class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j=nums[0]
        i=0
        while i < len(nums):
            if i>=len(nums)-1:
                return True
            if nums[i]==0 and i<len(nums):
                return False
            j=nums[i]
            i+=j
            