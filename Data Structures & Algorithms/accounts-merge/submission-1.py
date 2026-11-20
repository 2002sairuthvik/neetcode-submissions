class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj=defaultdict(list)
        email_to_name={}

        #connect accounts first email to other emails
        for acc in accounts:
            name=acc[0]
            first_email=acc[1]
            for email in acc[1:]:
                email_to_name[email]=name
                adj[first_email].append(email)
                adj[email].append(first_email)

        visit=set()
        res=[]

        def dfs(email,component):
            visit.add(email)
            component.append(email)
            for nei in adj[email]:
                if nei not in visit:
                    dfs(nei,component)
        
        for email in email_to_name:
            if email not in visit:
                component=[]
                dfs(email,component)
                res.append([email_to_name[email]] + sorted(component))
        return res







