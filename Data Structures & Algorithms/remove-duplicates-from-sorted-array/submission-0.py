class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums) and nums[i]==nums[j]:
                j+=1
            if j>i+1:
                del nums[i+1:j]
            i+=1
        return len(nums)