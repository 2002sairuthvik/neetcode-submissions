class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo(edges: List[List[int]]) -> List[int]:
            adj = defaultdict(list)
            for src, dst in edges:
                adj[src].append(dst)

            visit, path = set(), set()
            order = []

            def dfs(src: int) -> bool:
                if src in path:
                    return False
                if src in visit:
                    return True

                path.add(src)
                visit.add(src)
                for nei in adj[src]:
                    if not dfs(nei):
                        return False
                path.remove(src)
                order.append(src)
                return True

            for src in range(1, k + 1):
                if not dfs(src):
                    return []
            return order[::-1]
        
        row_order = topo(rowConditions)
        col_order = topo(colConditions)

        if not row_order or not col_order:
            return []

        row_pos = {num: r for r, num in enumerate(row_order)}
        col_pos = {num: c for c, num in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num

        return matrix