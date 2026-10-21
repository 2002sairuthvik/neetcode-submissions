class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:x[0])
        res=[]

        for query in queries:
            valid = []
            for start,end in intervals[::-1]:
                if start<=query<=end:
                    l = end-start+1
                    valid.append(l)
                if start>query:
                    continue
            if valid:
                min_int = min(valid)
                res.append(min_int)
            else:
                res.append(-1)
        return res