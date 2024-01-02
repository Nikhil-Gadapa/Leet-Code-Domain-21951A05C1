from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for element in tokens:
            if element.isdigit() or (element[0] == '-' and element[1:].isdigit()):
                stack.append(int(element))
            else:
                op2 = stack.pop()
                op1 = stack.pop()

                if element == '+':
                    stack.append(op1 + op2)
                elif element == '-':
                    stack.append(op1 - op2)
                elif element == '*':
                    stack.append(op1 * op2)
                elif element == '/':
                    # Ensure proper integer division
                    stack.append(int(op1 / op2))

        return stack[0]

# Example usage:
solution = Solution()
tokens = ["2", "1", "+", "3", "*"]
result = solution.evalRPN(tokens)
print(result)
