class Solution:
    def canJump(self, nums: List[int]) -> bool:
        rm = 0

        for i,jump in enumerate(nums):
            if i >rm:
                return False
            rm = max(rm,i+jump)
            if rm>=len(nums)-1:
                return True
        return True 