class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        # Track minimum bottleneck effort required to reach each cell
        efforts = [[float("inf")] * cols for _ in range(rows)]
        efforts[0][0] = 0

        # Min-heap stores (max_effort_along_path, row, col)
        min_heap = [(0, 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            curr_effort, r, c = heapq.heappop(min_heap)

            # First time target is popped from min-heap guarantees minimum possible effort
            if r == rows - 1 and c == cols - 1:
                return curr_effort

            # Skip stale heap entries if a cheaper path to (r, c) was already processed
            if curr_effort > efforts[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    step_diff = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(curr_effort, step_diff)

                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, nr, nc))

        return 0