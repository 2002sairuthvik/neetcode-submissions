class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        sd = defaultdict(list)

        for src,des in sorted(tickets,reverse=True):
            sd[src].append(des)

        route =[]

        def dfs(air):
            while sd[air]:
                next_dst = sd[air].pop()
                dfs(next_dst)
            # when an airport has no outgoing / it is last dest we add
            route.append(air)
        
        dfs("JFK")
        return route[::-1]