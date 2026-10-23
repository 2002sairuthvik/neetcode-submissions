class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(n):
            total=0
            while n:
                digit = n%10
                total+=digit*digit
                n=n//10
            return total
        slow=n
        fast = get_next(n)

        while fast!=1 and slow!=fast:
            slow= get_next(slow)
            fast = get_next(get_next(fast))
        return fast==1
