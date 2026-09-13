class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c_o  = {")":"(" , "]" : "[","}" : "{"}

        for c in s:
            if c in c_o:
                if stack and stack[-1] == c_o[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True