class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word=""
        m=len(word1)
        n=len(word2)
        i=0
        if m>n:
            while i<n:
                word+=word1[i]+word2[i]
                i+=1
            return word+word1[n:m]
        else:
            while i<m:
                word+=word1[i]+word2[i]
                i+=1
            return word+word2[m:n]
    