class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set() # r+c
        negDiag = set() # r-c
        res=[]
        board =[["."]*n for i in range(n)]

        def backtrack(r):
            # Base Case: all n queens placed successfully
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                # Check column and both diagonals in O(1)
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                # CHOOSE
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                # EXPLORE: move to the next row
                backtrack(r+1)

                # UNCHOOSE (Backtrack)
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res

