class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ma = 0
        stack = [] #idx,heights

        for i ,h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                idx,height = stack.pop()
                ma = max(ma,height*(i-idx))
                start = idx
            stack.append((start,h))
        for i,he in stack:
            ma = max(ma, he *(len(heights) - i))
        return ma
            