class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)

        def dfs(i,cur_xor):
            if i==n:
                return cur_xor
            include = dfs(i+1,cur_xor^nums[i])
            exclude = dfs(i+1,cur_xor)

            return include+exclude
        return dfs(0,0)