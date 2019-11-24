"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations. Questions to ask the interviewer :
Q: What should getMin() do on empty stack? 
A: In this case, return -1.

Q: What should pop do on empty stack? 
A: In this case, nothing. 

Q: What should top() do on empty stack?
A: In this case, return -1
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    # @param x, an integer
    def push(self, x):
        
        if self.stack == []:
            self.min_stack.append(x)
            self.stack.append(x)
            return
                 
                
        if x <= self.min_stack[-1]:#when push element is less then current min update curr_min
            self.min_stack.append(x)
            self.stack.append(x)
        else:
            self.stack.append(x)
        
    # @return nothing
    def pop(self):
        
        #if stack is empty return nothing
        if self.stack == []:
            return 
        
        ele = self.stack.pop()
        
        if ele <= self.min_stack[-1]:#when pop element is less then current min update curr_min
            self.min_stack.pop()
        
        

    # @return an integer
    def top(self):
        if self.stack != []:
            ele = self.stack[-1]
            return ele
        else:
            return -1

    # @return an integer
    def getMin(self):
        
        if self.stack == []:
            return -1
        else:
            return self.min_stack[-1]
