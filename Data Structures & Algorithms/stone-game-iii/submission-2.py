class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # d1 = dp[i + 1], d2 = dp[i + 2], d3 = dp[i + 3]
        d1 = d2 = d3 = 0

        for i in range(n - 1, -1, -1):
            best = float("-inf")
            take_sum = 0

            take_sum += stoneValue[i]
            best = max(best, take_sum - d1)

            if i + 1 < n:
                take_sum += stoneValue[i + 1]
                best = max(best, take_sum - d2)

            if i + 2 < n:
                take_sum += stoneValue[i + 2]
                best = max(best, take_sum - d3)

            d1, d2, d3 = best, d1, d2

        if d1 > 0:
            return "Alice"
        if d1 < 0:
            return "Bob"
        return "Tie"