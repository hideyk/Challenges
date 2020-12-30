class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.val = val

class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)
    
    def _add(self, val, node):
        if val < node.val:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        if val > node.val:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)
    
    def find(self, val):
        if self.root is None:
            return None
        else:
            return self._find(val, self.root)
    
    def _find(self, val, node):
        if val == node.val:
            return node
        elif val < node.val and node.l is not None:
            self._find(val, node.l)
        elif val > node.val and node.r is not None:
            self._find(val, node.r)

    def deleteNode(self, val):
        if self.root is None:
            return
        elif self.root.val == val:
            self.deleteTree()
        else:
            self._deleteNode(val, self.root)
    
    def _deleteNode(self, val, node):
        if node.l.val == val:
            node.l = None
            return
        if node.r.val == val:
            node.r = None
            return
        if node.val > val:
            self._deleteNode(val, node.l)
        else:
            self._deleteNode(val, node.r)


    def deleteTree(self):
        self.root = None
    
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
    
    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.val) + ' ')
            self._printTree(node.r)

def main():
    tree = Tree()
    tree.add(10)
    tree.add(2)
    tree.add(11)
    tree.add(1)
    tree.add(4)
    tree.deleteNode(2)
    tree.printTree()

if __name__ == "__main__":
    main()
