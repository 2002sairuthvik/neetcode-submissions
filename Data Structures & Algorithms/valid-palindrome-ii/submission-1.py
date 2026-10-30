class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skl,skr=s[l+1:r+1],s[l:r]
                return (skl==skl[::-1] or skr==skr[::-1])
            l+=1
            r-=1
        return True