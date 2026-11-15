class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

class Trie:
    def __init__(self,words:list[str]):
        self.root=TrieNode()
        for word in words:
            curr=self.root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch]=TrieNode()
                curr=curr.children[ch]
            curr.endOfWord=True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n=len(s)
        trie=Trie(wordDict)
        memo={n:[""]}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            res=[]
            curr=trie.root

            for j in range(i,n):
                ch=s[j]
                if ch not in curr.children:
                    break
                curr=curr.children[ch]

                if curr.endOfWord:
                    word=s[i:j+1]
                    for sub_sentence in dfs(j+1):
                        if sub_sentence:
                            res.append(word+" "+sub_sentence)
                        else:
                            res.append(word)
            memo[i]=res
            return res
        return dfs(0)







