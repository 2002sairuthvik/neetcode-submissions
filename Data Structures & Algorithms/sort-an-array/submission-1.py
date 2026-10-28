class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #Heap sort

        def heapify(length,i):
            largest=i
            left = 2*i+1
            right = 2*i+2

            while left < length and nums[left]>nums[largest]:
                largest=left
            while right<length and nums[right]>nums[largest]:
                largest=right
            
            if largest !=i:
                nums[i],nums[largest]=nums[largest],nums[i]
                heapify(length,largest)
        n=len(nums)

        for i in range(n//2,-1,-1):
            heapify(n,i)
        
        for i in range(n-1,0,-1):
            nums[0],nums[i]=nums[i],nums[0]
            heapify(i,0)
        return nums