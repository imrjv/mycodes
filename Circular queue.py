class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]* self.size
        self.front = self.rear = -1

    def enQueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full.")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def deQueue(self):
        if self.front == -1:
            print("Queue is Empty!")
        elif self.front == self.rear:
            print("Dequeued element is ", self.queue[self.front])
            self.front = self.rear = -1
        else:
            print("Dequeued element is ", self.queue[self.front])
            self.front = (self.front + 1) % self.size


q = CircularQueue(10)
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
q.enQueue(50)
q.enQueue(60)
q.deQueue()
q.enQueue(70)
q.enQueue(80)
q.deQueue()
q.enQueue(90)
print(q.front)
print(q.rear)
print(q.queue[q.rear])

''' 

Dequeued element is  10
Dequeued element is  20
2
8
90

'''
