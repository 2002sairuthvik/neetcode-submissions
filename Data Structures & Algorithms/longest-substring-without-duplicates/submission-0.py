class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        sub = 0
        for r in range(len(s)):
            char = s[r]

            if char in seen and seen[char]>=l:
                l = seen[char]+1

            seen[char] = r

            sub = max(sub, r-l+1)
        return sub