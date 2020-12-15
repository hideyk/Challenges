class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertFront(self, node):
        if not self.tail:
            self.tail = node
        if self.head:
            self.head.prev = node
            node.next = self.head
        self.head = node
    
    def insertBack(self, node):
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def removeFront(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head, self.tail = None, None
            return
        self.head = self.head.next
        self.head.prev = None

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
        a.insertFront(Node(i))
    for j in range(5, 10):
        a.insertBack(Node(j))
    for k in range(3):
        a.removeFront()
    a.printItems()

if __name__ == "__main__":
    main()