class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        Rows,Cols = len(matrix),len(matrix[0])

        for r in range(Rows):
            for c in range(r+1,Rows):
                matrix[r][c] ,matrix[c][r] = matrix[c][r] ,matrix[r][c]
        
        for r in range(Rows):
            matrix[r].reverse()
        
            