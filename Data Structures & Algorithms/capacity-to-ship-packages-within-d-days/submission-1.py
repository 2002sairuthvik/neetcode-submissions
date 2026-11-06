class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r

        def canShip(cap):
            days_used=1
            curr_cap=0
            for w in weights:
                if curr_cap+w>cap:
                    days_used+=1
                    curr_cap=0
                curr_cap+=w
            return days_used<=days           

        while l<=r:
            cap=(l+r)//2
            if canShip(cap):
                res=min(res,cap)
                r=cap-1
            else:
                l=cap+1
        return res