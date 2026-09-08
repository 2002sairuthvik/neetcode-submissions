class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        rk = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue
                bk = (r//3,c//3)

                if (val in rows[r] 
                or val in cols[c] or val in rk[bk]):
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                rk[bk].add(val)
        return True