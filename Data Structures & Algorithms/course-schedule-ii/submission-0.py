class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # building adj list for prerequisites
        pmap = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            pmap[crs].append(pre)
        
        # a course has 3 possible states:
        # visited -> crs has been added to output
        # visiting -> crs not added to output but added to current cycle or dfs 
        # unvisited -> crs  not added to output or cycle
        output = []
        cycle = set()    # Nodes currently in the active DFS path
        visited = set()  # Nodes fully explored and already added to output
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in pmap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output
                