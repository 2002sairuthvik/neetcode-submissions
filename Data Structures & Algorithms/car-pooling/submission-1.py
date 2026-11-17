class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes=[0]*1000

        for passengers,start,end in trips:
            changes[start]+=passengers
            changes[end]-=passengers
        
        cur_passengers=0
        for delta in changes:
            cur_passengers+=delta
            if cur_passengers>capacity:
                return False
        return True
        