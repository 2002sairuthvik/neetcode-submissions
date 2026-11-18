class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_idx = {ch: idx for idx, ch in enumerate(order)}
        # Convert each word to a tuple of integer ranks and verify non-decreasing order
        ranked = [[order_idx[ch] for ch in word] for word in words]
        return all(ranked[i] <= ranked[i + 1] for i in range(len(ranked) - 1))