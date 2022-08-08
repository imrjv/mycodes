class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class circularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
        else:
            newNode.next = newNode
            self.head = newNode

    def traversal(self, node):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.value, end=' ')
                temp = temp.next
                if temp == self.head:
                    break


cl = circularLinkedList()
cl.push(11)
cl.push(2)
cl.push(56)
cl.push(12)
cl.traversal(cl.head)
