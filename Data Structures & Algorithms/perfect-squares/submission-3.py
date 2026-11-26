class Solution:
    def numSquares(self, n: int) -> int:
        def is_square(x: int) -> bool:
            root = math.isqrt(x)
            return root * root == x

        # Case 1: n is already a perfect square
        if is_square(n):
            return 1

        # Case 2: Check Legendre's 3-square obstruction: n = 4^a * (8b + 7)
        temp = n
        while temp % 4 == 0:
            temp //= 4
        if temp % 8 == 7:
            return 4

        # Case 3: Check if n = a^2 + b^2 for some 1 <= a <= sqrt(n)
        for a in range(1, math.isqrt(n) + 1):
            if is_square(n - a * a):
                return 2

        # Case 4: By Lagrange's theorem, the only remaining possibility is 3
        return 3