class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r: int, c: int) -> int:
            # Base Case: out of bounds, water (0), or already visited
            if (
                not (0 <= r < rows and 0 <= c < cols)
                or grid[r][c] == 0
                or (r, c) in visited
            ):
                return 0

            # 1. Mark current cell permanently in visited
            visited.add((r, c))

            # 2. Accumulate: 1 (current) + area from all 4 directions
            return 1 + (
                dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )

        for r in range(rows):
            for c in range(cols):
                # Only initiate search if it's unvisited land
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))

        return max_area