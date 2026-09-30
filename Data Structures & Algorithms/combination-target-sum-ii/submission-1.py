class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        self.prev = -1
        def backtrack(pos,curr,target):
            if target == 0:
                res.append(curr.copy())
            if target <0:
                return
            for i in range(pos,len(candidates)):
                if candidates[i]== self.prev:
                    continue
                curr.append(candidates[i])
                backtrack(i+1,curr,target - candidates[i])
                curr.pop()
                self.prev=candidates[i]
        backtrack(0,[],target)
        return res
