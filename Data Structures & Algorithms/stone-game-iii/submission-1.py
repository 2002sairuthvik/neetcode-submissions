class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # dp[i] = max (current_player_score - opponent_score) starting at index i
        dp = [float("-inf")] * (n + 1)
        dp[n] = 0  # Base case: no stones left -> 0 score difference

        for i in range(n - 1, -1, -1):
            take_sum = 0
            for k in range(3):
                if i + k < n:
                    take_sum += stoneValue[i + k]
                    dp[i] = max(dp[i], take_sum - dp[i + k + 1])

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"