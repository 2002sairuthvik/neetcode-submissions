class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)-1
        i=0
        while i <len(s)//2:
            s[i],s[n-i]=s[n-i],s[i]
            i+=1
        