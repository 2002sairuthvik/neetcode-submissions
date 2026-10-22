class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        
        l,r = 0,len(matrix[0])-1
        top,bottom = 0,len(matrix)-1

        while l<=r and top<=bottom:
            # sweep top row (left to right)
            for i in range(l,r+1):
                res.append(matrix[top][i])
            top+=1

            #sweep right col (top to bottom)
            for i in range(top,bottom+1):
                res.append(matrix[i][r])
            r-=1
            
            if not (l<=r and top<=bottom):
                break

            #sweep bottom row (right to left)
            for i in range(r,l-1,-1):
                res.append(matrix[bottom][i])
            bottom-=1

            #sweep left col (bottom to top)
            for i in range(bottom,top-1,-1):
                res.append(matrix[i][l])
            l+=1
        return res