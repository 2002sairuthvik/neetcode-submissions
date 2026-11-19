class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead=set(deadends)
        if "0000" in dead or target in dead:
            return -1
        
        if target == "0000":
            return 0
        
        front={"0000"}
        back={target}
        visited = dead | {"0000",target}
        turns=0
        while front and back:
            if len(front) > len(back):
                front,back=back,front
            
            next_front=set()
            for curr in front:
                for i in range(4):
                    digit = int(curr[i])
                    for delta in (-1,1):
                        nxt = curr[:i]+str((digit+delta)%10)+curr[i+1:]
                        if nxt in back:
                            return turns+1
                        if nxt not in visited:
                            visited.add(nxt)
                            next_front.add(nxt)
            front=next_front
            turns+=1
        return -1
