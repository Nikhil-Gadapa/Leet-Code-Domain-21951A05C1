class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1  
        if len(self.pop_stack) == 0:
            while len(self.push_stack) > 0:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self) -> int:
        if self.empty():
            return -1  
        if len(self.pop_stack) == 0:
            while len(self.push_stack) > 0:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return len(self.push_stack) == 0 and len(self.pop_stack) == 0