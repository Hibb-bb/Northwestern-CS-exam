class Node:
    def __init__(self, val, mode):
        self.val=val
        self.child = []
        self.mode = mode

    def add(self, node):
        self.child.append(node)

    def search(self, node, goal):
        self.hist = []
        if self._haspath(node, goal):
            print(self.hist)
        else:
            print('no path')

    def _haspath(self, node, goal):
        if node is None:
            return False
        
        self.hist.append(node.val)
        if node.val == goal:
            return True
        temp = [self._haspath(c, goal) for c in node.child]
        if True in temp:
            return True
        else:
            self.hist.remove(self.hist[-1])
            return False


nodes= [Node('peoria', 'd'), Node('springfield', 'd'), Node('bloomington', 'r'), Node('naperville', 'd'), Node('decatur', 'r'), Node('jacksonville', 'r'), Node('chicago', 'r'), Node('evanston', 'r'), Node('rockford', 'r')]
root = nodes[0]
root.add(nodes[1])
root.add(nodes[2])
root.add(nodes[3])
root.child[0].add(nodes[4])
root.child[0].add(nodes[5])
root.child[2].add(nodes[6])
root.child[2].add(nodes[7])
root.child[2].add(nodes[8])


def count(r):

    if len(r.child) == 0:
        return 0
    num = 0
    for n in r.child:
        if n.mode == 'r':
            num+=1
        c=count(n)
        num += c
        # print(c)
    return num

# print(count(root))




root.search(root,'jacksonville')
root.search(root,'evanston')
