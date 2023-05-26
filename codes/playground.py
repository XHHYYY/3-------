import heapq
class Item:
    def __init__(self, priority):
        self.priority = priority
        
    def __lt__(self, other):
        return self.priority < other.priority
    
class B():
    def __init__(self, num):
        self.num = num
    
# a = [(1, Item(3, 3)), (1, Item(4, 3)), (3, Item(0, 0))]
b = [(Item(3), B(2)), (Item(3), B(5)), (Item(4), B(1)), (Item(5), B(0))]
heapq.heapify(b)
m = heapq.nsmallest(1, b)
print(m)