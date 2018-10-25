#!/usr/bin/env python3

# PTA 1151

class Node:
    def __init__(self, val, parent = None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = parent
    
    def is_leaf(self):
        return self.left is None and self.right is None

    def is_root(self):
        return self.parent is None

    def find(self, val):
        if self.val == val:
            return self
        
        node = None
        if self.left:
            node = self.left.find(val)

        if node:
            return node

        if self.right:
            node = self.right.find(val)
        
        return node
    def pre_order(self):
        print(self.val, end = ", ")
        if self.left is not None:
            self.left.pre_order()
        if self.right is not None:
            self.right.pre_order()
    
def build_tree(in_order, pre_order):
    if len(in_order) == 0:
        return None
    
    val = pre_order[0]
    in_index = in_order.index(val)
    in_left = in_order[:in_index]
    in_right = in_order[in_index + 1:]
    pre_left = pre_order[1:in_index + 1]
    pre_right = pre_order[in_index + 1: ]

    tree = Node(val)
    tree.left = build_tree(in_left, pre_left)
    tree.right = build_tree(in_right, pre_right)

    if tree.left is not None:
        tree.left.parent = tree
    if tree.right is not None:
        tree.right.parent = tree
    
    return tree

(n_pairs, m_len) = [int(i) for i in input().split()]
in_order = [int(i) for i in input().split()]
pre_order = [int(i) for i in input().split()]

query = []
for i in range(n_pairs):
    (u, v) = [int(i) for i in input().split()]
    query.append((u, v))
"""
n_pairs = 6 
m_len = 8
in_order = [7, 2, 3, 4, 6, 5, 1, 8]
pre_order = [5, 3, 7, 2, 6, 4, 8, 1]
query = [(2, 6), (8, 1), (7, 9), (12, -3), (0, 8), (99, 99)]
"""

tree = build_tree(in_order, pre_order)
#tree.pre_order()
#print("")

for q in query:
    u = tree.find(q[0])

    v = tree.find(q[1])
    if u is None and v is None:
        print("ERROR: {0} and {1} are not found.".format(q[0], q[1]))
    elif u is None:
        print("ERROR: {0} is not found.".format(q[0]))
    elif v is None:
        print("ERROR: {0} is not found.".format(q[1]))
    else:
        u_parents = []
        up = u
        while up is not None:
            u_parents.append(up)
            up = up.parent
        
        v_parents = []
        vp = v
        while vp is not None:
            v_parents.append(vp)
            vp = vp.parent

        u_parents.reverse()
        v_parents.reverse()

        l = min(len(v_parents), len(u_parents))
        ancestor = None
        for i in range(l):
            if u_parents[i] == v_parents[i]:
                ancestor = u_parents[i]
            else:
                break

        if u == ancestor:
            print("{0} is an ancestor of {1}.".format(u.val, v.val))
        elif v == ancestor:
            print("{0} is an ancestor of {1}.".format(v.val, u.val))
        else:
            print("LCA of {0} and {1} is {2}".format(u.val, v.val, ancestor.val))