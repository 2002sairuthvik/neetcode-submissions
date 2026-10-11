class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        queue = deque([0])
        visited = set()

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True
            if start in visited:
                continue
            visited.add(start)

            for end in range(start+1,len(s)+1):
                if s[start:end] in words:
                    queue.append(end)
        return False