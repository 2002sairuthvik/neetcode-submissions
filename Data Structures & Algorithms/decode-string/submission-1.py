class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                # 1. Collect characters until '['
                sub_chars = []
                while stack and stack[-1] != '[':
                    sub_chars.append(stack.pop())
                stack.pop()  # Discard '['

                substr = "".join(reversed(sub_chars))

                # 2. Collect consecutive digits for multiplier k
                k_chars = []
                while stack and stack[-1].isdigit():
                    k_chars.append(stack.pop())

                k = int("".join(reversed(k_chars)))

                # 3. Push expanded string back onto stack
                stack.append(substr * k)

        return "".join(stack)