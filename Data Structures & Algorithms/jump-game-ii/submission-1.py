class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_end = 0
        farthest = 0

        for i in range(len(nums)-1):
            # we are iterating till last-2 because we know that at that point we can reach the final index from there so that would add extra jump
            farthest = max(farthest,i+nums[i])

            if i==curr_end:
                jumps+=1
                curr_end=farthest
                if curr_end>=len(nums)-1:
                    break
        return jumps
            