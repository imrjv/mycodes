class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def enQueue(self, item):
        temp = Node(item)
        if self.rear == None:
            self.rear = self.front = temp
            return
        self.rear.next = temp
        self.rear = temp

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        temp = self.front
        self.front = temp.next


q = queue()
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
q.enQueue(50)
q.deQueue()
q.deQueue()
print("Front element of the queue is ", q.front.data)
print("Rear element of the queue is ", q.rear.data)

'''

Front element of the queue is 30
Rear element of the queue is 50

Time complexity for enqueue and dequeue is O(1).
'''
