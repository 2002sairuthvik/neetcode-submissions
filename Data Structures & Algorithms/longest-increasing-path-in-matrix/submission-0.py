class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix and not matrix[0]:
            return 0

        rows,cols = len(matrix), len(matrix[0])
        dp = {} #(r,c) keep track of increasing path for each position

        def dfs(r,c):
            if (r,c) in dp:
                return dp[(r,c)]
            res = 1
            directions = [(1,0),(0,1),(-1,0),(0,-1)]

            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and matrix[nr][nc] > matrix[r][c]:
                    res = max(res,1+dfs(nr,nc))
            dp[(r,c)]=res
            return res
        max_path=0
        for r in range(rows):
            for c in range(cols):
                max_path = max(max_path,dfs(r,c))
        return max_path