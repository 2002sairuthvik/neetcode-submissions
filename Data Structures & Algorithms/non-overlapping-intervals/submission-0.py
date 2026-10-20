class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key=lambda i:i[0])
        prev_end = intervals[0][1]

        for start,end in intervals[1:]:
            if start<prev_end:
                #overlapping occured
                res+=1
                prev_end = min(end,prev_end)
            else:
                prev_end=end
        return res
            