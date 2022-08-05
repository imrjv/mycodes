class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            temp = self.head
            while temp.next is not None:
                print(temp.value, end=' ')
                temp = temp.next
            print(temp.value)

    def insertionStart(self, newData):
        temp = self.head
        new = Node(newData)
        new.next = temp
        self.head = new

    def insertionEnd(self, newData):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(newData)

    def afterNode(self,prevNode, newData):
        if prevNode is None:
            print("The given node does not exist in the linked list!")
        else:
            prev = prevNode
            next = prevNode.next
            new = Node(newData)
            prev.next = new
            new.next = next


ll = linkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
ll.head.next = second
second.next = third
third.next = fourth
# fourth.next = fifth
ll.display()
ll.insertionStart(7)
ll.display()
ll.insertionEnd(9)
ll.display()
ll.afterNode(ll.head.next, 11)
ll.display()
