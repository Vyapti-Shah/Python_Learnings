#Stack: LIFO (last in, first out). Typical ops: push (append), pop.
#Queue: FIFO (first in, first out). Use collections.deque for O(1) append/pop from both ends. queue.Queue is for multi-threading.

stack = []
stack.append(1)   # push
stack.append(2)
top = stack.pop() # pop -> 2
print(stack)

class stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
s = stack()
s.push(10) 
s.push(15)
s.push(20)
top1 = s.pop() # -> 20
print(s.items)



from collections import deque
q = deque()
q.append(1)       # enqueue at right
q.append(2)
item = q.popleft()# dequeue from left -> 1
print(q)

class queue:
    def __init__(self):
        self.items = deque()
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.popleft()
    def size(self):
        return len(self.items)
q1 = queue()
q1.enqueue(10)
q1.enqueue(15)
q1.enqueue(20)
item1 = q1.dequeue() # -> 1
print(q1.items) 