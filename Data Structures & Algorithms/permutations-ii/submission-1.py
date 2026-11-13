class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = {}
        for n in nums:
            count[n]=1+count.get(n,0)
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