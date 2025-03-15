class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
# bfs algorithm is chosed to explore tree structure.
# Nodes are pu in arrays based on their levels.
# Priority to put into array belongs to leftmost nodes.
def smallestSubset(node):
    queue = [node]
    depth = -1
    res = []
    while queue:
        length = len(queue)
        depth += 1
        res.append([])
        for _ in range(length):
            current = queue.pop(0)
            res[depth].append(current) 
            if current.left: queue.append(current.left) # priority on leftmost nodes
            if current.left: queue.append(current.right)
    
    # Deepest nodes are in res[-1]
    # Parent of deepest nodes reside in res[-2] 
    # Find the parent of deepest nodes
    for n in res[-2]:
        if n.left is not None or n.right is not None:
            return n

if __name__ == "__main__":
    n3 = Node(3)
    n5 = Node(5)
    n1 = Node(1)
    n6 = Node(6)
    n2 = Node(2)
    n1 = Node(1)
    n0 = Node(0)
    n8 = Node(8)
    n7 = Node(7)
    n4 = Node(4)
    n9 = Node(9)
    n3.left = n5
    n3.right = n1
    n5.left = n6
    n5.right = n2
    n1.left = n0
    n1.right = n8
    n2.left = n7
    n2.right = n4
    n8.right = n9

    sub = smallestSubset(n3)
    print(sub.val)