class Node:
    def __init__(self):
        self.right = None
        self.left = None

def calculateMaxDepth(n):
    if n is None:
        return 0
    else:
        lDepth = calculateMaxDepth(n.left)
        rDepth = calculateMaxDepth(n.right)

        if lDepth > rDepth:
            return lDepth+1
        else:
            return rDepth+1
        
node = Node()
node.left = Node()
node.left.left = Node()
node.left.left.left = Node()
node.left.left.left.left = Node()
node.left.left.left.left.left = Node()

print(calculateMaxDepth(node))
