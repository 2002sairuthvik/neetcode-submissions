class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort_dfs(conditions: List[List[int]]) -> List[int]:
            adj = defaultdict(list)
            for u, v in conditions:
                adj[u].append(v)

            # 0 = unvisited, 1 = visiting (in current recursion stack -> cycle!), 2 = visited
            state = [0] * (k + 1)
            order = []

            def dfs(node: int) -> bool:
                if state[node] == 1:
                    return False  # Directed cycle detected
                if state[node] == 2:
                    return True

                state[node] = 1
                for nxt in adj[node]:
                    if not dfs(nxt):
                        return False
                state[node] = 2
                order.append(node)
                return True

            for i in range(1, k + 1):
                if state[i] == 0 and not dfs(i):
                    return []

            return order[::-1]  # Reverse post-order gives topological order

        row_order = topo_sort_dfs(rowConditions)
        col_order = topo_sort_dfs(colConditions)

        if not row_order or not col_order:
            return []

        row_pos = {num: r for r, num in enumerate(row_order)}
        col_pos = {num: c for c, num in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num

        return matrix