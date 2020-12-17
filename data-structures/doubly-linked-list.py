class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertFront(self, value):
        newNode = Node(value)
        if not self.tail:
            self.tail = newNode
        if self.head:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode
    
    def insertBack(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
        if self.tail:
            self.tail.next = newNode
            newNode.prev = self.tail
        self.tail = newNode

    def removeFront(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head, self.tail = None, None
            return
        self.head = self.head.next
        self.head.prev = None

    def removeBack(self):
        if not self.tail:
            return
        if self.head == self.tail:
            self.head, self.tail = None, None
            return
        self.tail = self.tail.prev
        self.tail.next = None
    
    def insertAfter(self, prevNode, value):
        if prevNode is None:
            return
        newNode = Node(value)
        newNode.next = prevNode.next
        newNode.prev = prevNode
        prevNode.next = newNode
        if newNode.next:
            newNode.next.prev = newNode

    def printItems(self):
        auxilaryNode = self.head
        while auxilaryNode:
            print(auxilaryNode.value, end=" ")
            auxilaryNode = auxilaryNode.next

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


def main():
    a = DoubleLinkedList()
    for i in range(5):
        a.insertFront(i)
    for j in range(5, 10):
        a.insertBack(j)
    for k in range(3):
        a.removeFront()
    a.printItems()

if __name__ == "__main__":
    main()