class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        for digit in digits:
            total = total*10+digit
        total+=1

        res=[]
        while total>0:
            res.append(total%10)
            total//=10
        res.reverse()
        return res