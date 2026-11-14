class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        if total%k !=0:
            return False
        target = total//k
        nums.sort(reverse=True)
        if nums[0]>target:
            return False
        subsets=[0]*k
        def backtrack(i):
            if i==len(nums):
                return True
            seen=set()
            for j in range(3):
                if subsets[j]+nums[i]<=target and subsets[j] not in seen:
                    subsets[j]+=nums[i]
                    seen.add(subsets[j])

                    if backtrack(i+1):
                        return True
                    
                    subsets[j]-=nums[i]
                    if subsets[j]==0:
                        break
            return False
        return backtrack(0)
                    