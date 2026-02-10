import heapq

class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []
    def push(self, item):
        "Push 'item' onto the stack"
        self.list.append(item)
    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()
    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0

class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []
    def push(self, item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)
    def pop(self):
        "Dequeue the earliest enqueued item"
        return self.list.pop()
    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0

class PriorityQueue:
    """
    Implements a priority queue data structure. Each inserted item
    has a priority associated with it. The client is usually responsible
    for calculating this priority (f = g + h).
    """
    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0