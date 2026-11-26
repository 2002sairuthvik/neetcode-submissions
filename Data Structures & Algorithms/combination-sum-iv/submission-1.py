class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo={0:1}

        def dfs(rem):
            if rem in memo:
                return memo[rem]
            
            ways=0
            for num in nums:
                if rem>=num:
                    ways+=dfs(rem-num)
            
            memo[rem]=ways
            return ways
        
        return dfs(target)