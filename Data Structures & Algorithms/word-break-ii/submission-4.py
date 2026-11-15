class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        word_set = set(wordDict)
        max_len = max((len(w) for w in wordDict), default=0)
        memo = {n: [""]}

        def dfs(i: int) -> List[str]:
            if i in memo:
                return memo[i]

            res = []
            # Only check up to i + max_len
            for j in range(i, min(n, i + max_len)):
                word = s[i : j + 1]
                if word in word_set:
                    for sub in dfs(j + 1):
                        res.append(word + (" " + sub if sub else ""))

            memo[i] = res
            return res

        return dfs(0)