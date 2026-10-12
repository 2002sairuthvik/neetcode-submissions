class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dm = {c : text1.count(c) for c in text1}
        count=0
        for ch in text2:
            if ch in dm:
                count+=1
        return count