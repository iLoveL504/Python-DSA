from collections import deque
# binary tree
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
         
    def __str__(self):
        return str(self.val)
    
    # Pre order traversal
    def pre_order(self, node):
        if not node:
            return
        
        print(node)
        self.pre_order(node.left)
        self.pre_order(node.right)

    # In order traversal
    def in_order(self, node):
        if not node:
            return
        self.in_order(node.left)        
        print(node)

        self.in_order(node.right)

    # Post order traversal 4, 5, 2, 10, 3, 1
    def post_order_recursive(self, node):
        if not node:
            return
        self.post_order_recursive(node.left)
        self.post_order_recursive(node.right)
        print(node)

    # FInall figured this out
    # thought process for this
    # stack for post order left right root
    # stack = [4,]
    # stk1 = [1, 3, 10, 2, 5, 8, 7,]
    # stk1 = [1, 3, 10, 2, 5, 8, 7, 4]


    # correct order: 4, 7, 8, 5, 2, 10, 3, 1
    # stack should look like [1, 3, 10, 2, 5, 8, 7, 4]
    def post_order_iterative(self, node):
        stk = [node]
        stk1 = []

        while stk:
            node = stk.pop()
            stk1.append(node)
            if node.left: stk.append(node.left)
            if node.right: stk.append(node.right)
        while stk1:
            print(stk1.pop())





    #     while stk1:


    
    # Iterative Pre Order Traversal 
    def pre_order_iterative(self, node):
        stk = [node]
        while stk:
            node = stk.pop()
            print(node)
            if node.right: stk.append(node.right)
            if node.left: stk.append(node.left)

    # Level Order Traversal (BFS) Time: O(n), Space: O(n) 
    def level_order(self, node):
        q = deque()
        q.append(node)

        while q:
            node = q.popleft()
            print(node)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

    # Check if Value Exists (DFS) Time: O(n), Space: O(n)
    def search(self, node, target):
        if not node:
            return False
        
        if node.val == target:
            return True
        
        return self.search(node.left, target) or self.search(node.right, target)
    
    # Time: O(log n), Space: O(log n)
    def search_bst(self, node, target):
        if not node:
            return False
        
        if node.val == target:
            return True
        
        if target < node.val: return self.search_bst(node.left, target)
        else: return self.search_bst(node.right, target)

A = TreeNode(1);    
B = TreeNode(2);    
C= TreeNode(3);    
D = TreeNode(4);    
E = TreeNode(5);    
F = TreeNode(10)
G = TreeNode(7)
H = TreeNode(8)   

A.left = B
A.right = C
B.left = D

B.right = E
E.left = G
E.right = H
C.left = F 

A.post_order_iterative(A)
# A.level_order(A)
# print(A.search(A, 5))


# Binary Search Trees 

# A2 = TreeNode(5);    
# B2 = TreeNode(1);    
# C2 = TreeNode(8);    
# D2 = TreeNode(-1);    
# E2 = TreeNode(3);    
# F2 = TreeNode(7);   
# G2 = TreeNode(9);   

# A2.left, A2.right = B2, C2
# B2.left, B2.right = D2, E2
# C2.left, C2.right = F2, G2

# A2.in_order(A2)
