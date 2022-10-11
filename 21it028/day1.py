class stack:
    def __init__(self):
        self.stack = list()
    def push(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        return False
    def pop(self):
        if len(self.stack)<=0:
            return ("stack empty!")
        return self.stack.pop()
    def size(self):
            return len(self.stack)
mystack = stack()
print(mystack.push(5))
print(mystack.push(6))
print(mystack.push(9))
print(mystack.push(5))
print(mystack.push(3))
print(mystack.size())
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
print(mystack.size())
print(mystack.pop())
333333333333
