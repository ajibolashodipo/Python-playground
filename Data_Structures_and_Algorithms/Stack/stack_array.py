class Stack:
    def __init__(self):
        self.items=[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items)==0

    def peek(self):
        last_index= len(self.items)-1
        return self.items[last_index]

    def get_stack(self):
        return self.items


a= Stack()
a.push("A")
a.push("B")
a.push("C")
a.pop()

print(a.get_stack())
print(a.isEmpty())
print(a.peek())
print([0]*5)