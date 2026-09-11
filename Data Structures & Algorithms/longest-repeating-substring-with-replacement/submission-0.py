class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map={}
        l = 0
        max_freq = 0
        max_l = 0
        for r in range(len(s)):
            map[s[r]] = map.get(s[r],0)+1
            max_freq = max(max_freq,map[s[r]])

            while r-l+1 - max_freq >k:
                map[s[l]]-=1
                l+=1
            
            max_l = max(max_l,r-l+1)
        return max_l