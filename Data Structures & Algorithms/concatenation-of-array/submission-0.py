class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = 2*len(nums)

        for n in range(len(nums),n):
            nums.append(nums[n%4])
        
        return nums
