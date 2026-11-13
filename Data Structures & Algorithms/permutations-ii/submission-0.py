class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res=[]
        path=[]

        def backtrack():
            if len(path)==len(nums):
                res.append(path[:])
                return
            for num in count:
                if count[num]>0:
                    #choose
                    path.append(num)
                    count[num]-=1
                    #explore
                    backtrack()
                    #unchoose
                    count[num]+=1
                    path.pop()
        backtrack()
        return res