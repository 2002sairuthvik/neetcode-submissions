class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]* len(temperatures)
        stack = [] # we add pair : temperatures,index
        for i ,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIn = stack.pop()
                res[stackIn]  = i - stackIn
            stack.append([t,i])
        return res