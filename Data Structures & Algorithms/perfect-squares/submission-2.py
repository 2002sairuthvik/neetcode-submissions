class Solution:
    def numSquares(self, n: int) -> int:
        squares=[k*k for k in range(1,int(n**0.5)+1)]
        queue=deque([(n,0)]) #remaining_sum,steps_taken
        visited={n}
        while queue:
            rem,steps=queue.popleft()
            for sq in squares:
                nxt=rem-sq
                if nxt==0:
                    return steps+1
                if nxt<0:
                    break
                if nxt>0:
                    visited.add(nxt)
                    queue.append((nxt,steps+1))
        return n
