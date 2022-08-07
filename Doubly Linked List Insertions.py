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

    def insertAfter(self, node, data):
        newNode = Node(data)
        if node is None:
            print("The given node does not exist in the linked list!")
        else:
            newNode = Node(data)
            prev = node
            next = prev.next
            prev.next = newNode
            newNode.next = next
            newNode.prev = prev
            next.prev = newNode

    def endAdd(self, data):
        node = self.head
        newNode = Node(data)
        while node.next is not None:
            node = node.next
        node.next = newNode
        newNode.prev = node
        newNode.next = None

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
        print()


dl = doublyLinkedList()
dl.head = Node(1)
dl.addFront(2)
dl.addFront(3)
dl.addFront(5)
dl.traversal(dl.head)
dl.insertAfter(dl.head.next, 11)
dl.traversal(dl.head)
dl.endAdd(88)
dl.traversal(dl.head)


