class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        num = 0
        sign = '+'
        i = 0
        
        while i < len(s):
            char = s[i]

            if char.isdigit():
                num = num * 10 + int(char)

            if not char.isdigit() or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    prev = stack.pop()
                    stack.append(int(prev / num))  # truncates toward 0

                sign = char
                num = 0

            i += 1

        return sum(stack)
