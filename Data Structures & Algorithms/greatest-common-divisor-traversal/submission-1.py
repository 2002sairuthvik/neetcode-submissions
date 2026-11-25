class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if 1 in nums:
            return False

        # Bipartite adjacency maps: index <-> prime factors
        idx_to_primes = defaultdict(list)
        prime_to_indices = defaultdict(list)

        for i, val in enumerate(nums):
            d = 2
            temp = val
            while d * d <= temp:
                if temp % d == 0:
                    idx_to_primes[i].append(d)
                    prime_to_indices[d].append(i)
                    while temp % d == 0:
                        temp //= d
                d += 1
            if temp > 1:
                idx_to_primes[i].append(temp)
                prime_to_indices[temp].append(i)

        # Standard BFS starting from index 0
        queue = deque([0])
        visited_indices = {0}
        visited_primes = set()

        while queue:
            curr_idx = queue.popleft()
            for p in idx_to_primes[curr_idx]:
                if p not in visited_primes:
                    visited_primes.add(p)
                    for nei_idx in prime_to_indices[p]:
                        if nei_idx not in visited_indices:
                            visited_indices.add(nei_idx)
                            queue.append(nei_idx)

        return len(visited_indices) == n