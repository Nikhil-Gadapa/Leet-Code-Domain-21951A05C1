class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        s=0
        for op in operations:
            if op=='C':
                s-=stack.pop()
            elif op=='D':
                stack.append(2*stack[-1])
                s+=2*stack[-1]
            elif op=="+":
                stack.append(stack[-1]+stack[-2])
                s+=stack[-1]
            else:
                stack.append(int(op))
        return sum(stack)