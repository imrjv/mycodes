class priorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        if len(self.queue) == 0:
            return "Queue is Empty!"

    def insert(self, item):
        self.queue.append(item)

    def delete(self):
        maxValue = 0
        for i in range(len(self.queue)):
            if self.queue[i] > self.queue[maxValue]:
                maxValue = i
        value = self.queue[maxValue]
        del self.queue[maxValue]
        return value


pq = priorityQueue()
print(pq.isEmpty())
pq.insert(1)
pq.insert(2)
pq.insert(3)
pq.insert(4)
pq.insert(5)
print(pq.delete(), end=' ')
print(pq.delete())
print(pq)
