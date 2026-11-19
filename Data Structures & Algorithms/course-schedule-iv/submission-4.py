class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        prereq_map = defaultdict(set)  # course -> set of all prerequisites

        for pre, crs in prerequisites:
            adj[pre].append(crs)
            in_degree[crs] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while queue:
            curr = queue.popleft()
            for nxt in adj[curr]:
                # nxt inherits curr as a prerequisite, plus all of curr's prerequisites
                prereq_map[nxt].add(curr)
                prereq_map[nxt] |= prereq_map[curr]

                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)

        return [u in prereq_map[v] for u, v in queries]