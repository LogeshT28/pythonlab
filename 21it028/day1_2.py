class stack:
    def __init__(self):
        self.stack = list()
        self.maxsize = 8
        self.top = 0
    def push(self,data):
        if self.top>= self.maxsize:
            return ("stack full!")
        self.stack.append(data)
        self.top+= 1
        return True
    def pop(self):
        if self.top<=0:
            return ("stack empty!")
        item = self.stack.pop()
        self.top-=1
        return item
    def size(self):
        return self.top
s= stack()
    
print(s.push(1))
print(s.push(2))
print(s.push(3))
print(s.push(4))
print(s.push(5))
print(s.push(6))
print(s.push(7))
print(s.push(8))
print(s.push(9))

print(s.size())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
