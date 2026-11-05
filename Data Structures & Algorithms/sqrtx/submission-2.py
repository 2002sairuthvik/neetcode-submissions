# class Solution:
#     def mySqrt(self, x: int) -> int:
#        l,r=0,x
#        while l<=r:
#         m=(l+r)//2
#         s=m*m
#         if s==x:
#             return m
#         elif s>x:
#             r=m-1
#         else:
#             l=m+1
#         return r
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            m = (l + r) // 2
            square = m * m

            if square == x:
                return m
            elif square > x:
                r = m - 1
            else:
                l = m + 1

        # At termination, r is the greatest integer satisfying r^2 <= x
        return r
