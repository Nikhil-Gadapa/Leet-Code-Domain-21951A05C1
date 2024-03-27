class MyQueue:
    def __init__(self):
        self.stack=[]
        
    def push(self,x:int)->None:
        self.stack.append(x)
        
    def pop(self)->int:
        return self.stack.pop(0)
    
    def peek(self):
        return self.stack[0]
    def empty(self):
        return len(self.stack)==0
    
