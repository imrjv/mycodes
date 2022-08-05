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

    def deletionStart(self):
        temp = self.head
        if temp is None:
            print("There is no elements present in the linked list!")
        else:
            next = temp.next
            self.head = next

    def deletionEnd(self):
        temp = self.head
        if temp is None:
            print("There is no elements present in the linked list!")
        else:
            while temp.next is not None:
                prev = temp
                temp = temp.next
            prev.next = None

    def afterEle(self, prevNode):
        if prevNode is None:
            print("The given element does not exist in the linked list!")
        else:
            if prevNode.next is not None:
                new = prevNode.next
                new1 = new.next
                prevNode.next = new1



ll = linkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
ll.head.next = second
second.next = third
third.next = fourth
ll.display()
ll.deletionStart()
ll.display()
ll.deletionEnd()
ll.display()
ll.afterEle(ll.head)
ll.display()
