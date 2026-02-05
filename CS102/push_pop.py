class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
    def pop(self):
        if len(self.items) == 0:
            print("Cannot pop from empty stack")
            return None
        return self.items.pop()

s = Stack()
s.push("Spider-Man #1")
s.push("Batman #27")
s.push("X-Men #5")

print(s.pop())   # top comic
print(s.pop())   # next comic
print(s.pop())   # last comic
print(s.pop())   # triggers the empty warning
