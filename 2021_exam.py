import math



class Tree:
    def __init__(self):
        self.root = None

    def add_root(self, node):
        self.root = node

    def count_nodes(self):
        self.count = 0
        self._traverse_nodes(self.root)
        print('total nodes', self.count-1)

    def count_terminals(self):
        self.termins = 0
        self._traverse_terminals(self.root)
        print('terminals', self.termins)

    def _traverse_terminals(self, node):

        for n in node.cases:
            try:
                self._traverse_terminals(n)
            except:
                self.termins += 1

    def _traverse_nodes(self, node):
        if node is None:
            return 0
        else:
            self.count += 1
            for n in node.cases:
                try:
                    self._traverse_nodes(n)
                except:
                    pass

    def find_path(self, cur_node, next_goal):
        found = False
        for i, n in enumerate(cur_node.cases):
            if n.name == next_goal:
                self.p *= cur_node.probs[i]
                cur_node = n
                found = True
                break
        if found is True:
            return cur_node
        else:
            return None

    def traverse_to_goal(self, path):
        
        self.p = 1
        
        cur_node = self.root
        path_idx = 0
        next_goal = path[path_idx]

        while(True):
            n = self.find_path(cur_node, next_goal)
            if path_idx == len(path)-1:
                break
            if n is None:
                self.p = 0
            else:
                cur_node = n
                path_idx += 1
                next_goal = path[path_idx]
            
        print('path to', path ,'prob:',self.p, 1/9)


class Node:
    def __init__(self, name, cases=None, probs=None):

        self.name = name

        if cases is not None and probs is not None:

            if len(cases) != len(probs):
                raise Exception('case and probability amount does not match')
            if sum(probs) != 1:
                raise Exception('probability sum not equal to 1')

        self.cases = cases # a list of nodes or cases
        self.probs = probs # a list of probabilities



exp = Tree()
h = Node('h')
t = Node('t')
c1 = Node('c1',[h, t], [1/3, 2/3])
c2 = Node('c2',[h, t], [1/4, 3/4])
c3 = Node('c3',[h, t], [1/5, 4/5])
coin_selection = Node('selection',[c1, c2, c3], [1/3, 1/3, 1/3])

exp.add_root(coin_selection)
exp.count_nodes()
exp.count_terminals()
exp.traverse_to_goal(['c1', 'h'])
exp.traverse_to_goal(['c3', 't'])
