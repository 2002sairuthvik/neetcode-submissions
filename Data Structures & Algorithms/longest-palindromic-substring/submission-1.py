class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        for i in range(len(s)):
            # 1. Odd length center (e.g., "aba")
            p1 = self.expand(s, i, i)
            if len(p1) > len(res):
                res = p1
                
            # 2. Even length center (e.g., "abba")
            p2 = self.expand(s, i, i + 1)
            if len(p2) > len(res):
                res = p2

        return res

    def expand(self, s: str, l: int, r: int) -> str:
        # Expand outward as long as characters match
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            
        # Return the valid palindrome substring found.
        # Note: We use l + 1 because the loop decremented 'l' one step too far before breaking.
        return s[l + 1 : r]
