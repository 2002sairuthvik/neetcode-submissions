class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in visited:
            return -1
        
        queue=deque([("0000",0)])
        visited.add("0000")

        while queue:
            curr,turns=queue.popleft()

            if curr==target:
                return turns
            
            for i in range(4):
                digit=int(curr[i])
                for delta in (-1,1):
                    next_digit = (digit+delta)%10
                    next = curr[:i]+str(next_digit)+curr[i+1:]

                    if next not in visited:
                        visited.add(next)
                        queue.append((next,turns+1))
        return -1

