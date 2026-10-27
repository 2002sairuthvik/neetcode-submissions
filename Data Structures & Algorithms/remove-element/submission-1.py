class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for num in nums[:]:
            if num==val:
                nums.remove(num)
        k=len(nums)
        return k