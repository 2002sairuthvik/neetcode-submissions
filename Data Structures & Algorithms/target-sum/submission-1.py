class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        # Edge cases: impossible target or non-integer subset sum
        if total < abs(target) or (target + total) % 2 != 0:
            return 0
        subset_target = (target+total)//2

        dp = [0]*(subset_target+1)
        dp[0] = 1 # one way to form sum 0

        for n in nums:
            # Iterate backwards down to n to prevent using n multiple times
            for s in range(subset_target-1,-1,-1):
                dp[s]+=dp[s-n]
        return dp[subset_target]