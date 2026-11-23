class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[ry] = rx

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        if rows == 1 and cols == 1:
            return 0

        edges = []
        for r in range(rows):
            for c in range(cols):
                curr_id = r * cols + c
                if r + 1 < rows:
                    edges.append((abs(heights[r][c] - heights[r + 1][c]), curr_id, (r + 1) * cols + c))
                if c + 1 < cols:
                    edges.append((abs(heights[r][c] - heights[r][c + 1]), curr_id, r * cols + (c + 1)))

        edges.sort(key=lambda x: x[0])
        uf = UnionFind(rows * cols)
        target = rows * cols - 1

        for diff, u, v in edges:
            uf.union(u, v)
            if uf.find(0) == uf.find(target):
                return diff

        return 0 