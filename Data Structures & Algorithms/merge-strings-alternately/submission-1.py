class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word=""
        m=len(word1)
        n=len(word2)
        if m>n:
            m,n=n,m
            word1,word2=word2,word1
        i=0
        while i<m:
            word+=word1[i]+word2[i]
            i+=1
        return word+word2[m:n]