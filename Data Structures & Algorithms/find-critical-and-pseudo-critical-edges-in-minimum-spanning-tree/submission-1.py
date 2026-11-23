class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        self.components -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Preserve original index before sorting by edge weight ascending
        indexed_edges = [
            (u, v, w, idx) for idx, (u, v, w) in enumerate(edges)
        ]
        indexed_edges.sort(key=lambda x: x[2])

        def run_kruskal(banned_idx: int = -1, forced_edge: tuple = None) -> float:
            uf = UnionFind(n)
            total_weight = 0

            # If testing pseudo-critical: force this edge into the MST first
            if forced_edge is not None:
                u, v, w, _ = forced_edge
                if uf.union(u, v):
                    total_weight += w

            for u, v, w, idx in indexed_edges:
                if idx == banned_idx:
                    continue
                if uf.union(u, v):
                    total_weight += w
                    if uf.components == 1:
                        break

            return total_weight if uf.components == 1 else float("inf")

        # Step 1: Compute baseline MST weight
        base_mst_weight = run_kruskal()

        critical = []
        pseudo_critical = []

        # Step 2: Classify every edge using exclusion first, then forced inclusion
        for edge in indexed_edges:
            _, _, _, orig_idx = edge

            # Test 1: Does banning this edge increase MST weight (or disconnect graph)?
            if run_kruskal(banned_idx=orig_idx) > base_mst_weight:
                critical.append(orig_idx)
            # Test 2: Otherwise, can forcing this edge still achieve base_mst_weight?
            elif run_kruskal(forced_edge=edge) == base_mst_weight:
                pseudo_critical.append(orig_idx)

        return [critical, pseudo_critical]