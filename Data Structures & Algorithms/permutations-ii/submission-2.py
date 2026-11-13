class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        perms=[]
        visited=[False]*len(nums)

        def dfs():
            if len(perms)==len(nums):
                res.append(perms.copy())
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not visited[i-1]:
                    continue
                visited[i]=True
                perms.append(nums[i])
                dfs()
                visited[i]=False
                perms.pop()
        dfs()
        return res