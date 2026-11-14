class Solution:
    def totalNQueens(self, n: int) -> int:
        full_mask = (1 << n) - 1

        def backtrack(r: int, cols: int, d1: int, d2: int) -> int:
            if r == n:
                return 1

            count = 0
            # Bitmask of all safe columns in current row r
            available = full_mask & ~(cols | d1 | d2)

            while available:
                # Isolate lowest set bit (rightmost valid column)
                bit = available & -available
                # Clear that bit from available choices
                available ^= bit

                # Shift diagonals as we move down one row:
                # '/' diagonal shifts left (<< 1), '\' diagonal shifts right (>> 1)
                count += backtrack(
                    r + 1,
                    cols | bit,
                    (d1 | bit) << 1,
                    (d2 | bit) >> 1,
                )

            return count

        return backtrack(0, 0, 0, 0)