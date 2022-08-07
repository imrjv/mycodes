class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None


class doublyLinkedList:
    def __init__(self):
        self.head = None

    def addFront(self, data):
        newNode = Node(data)
        newNode.next = self.head
        newNode.prev = None
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    def traversal(self, node):
        print("Traversal in forward direction: ", end=' ')
        last = None
        while node:
            print(node.value, end=' ')
            last = node
            node = node.next

        print()
        print("Traversal in backword direction: ", end=' ')
        while last:
            print(last.value, end=' ')
            last = last.prev


dl = doublyLinkedList()
dl.head = Node(1)
dl.addFront(2)
dl.addFront(3)
dl.addFront(5)
dl.traversal(dl.head)




