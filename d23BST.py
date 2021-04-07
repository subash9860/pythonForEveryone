# Task
# A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom. You are given a pointer, , pointing to the root of a binary search tree. Complete the levelOrder function provided in your editor so that it prints the level-order traversal of the binary search tree.

# Hint: You'll find a queue helpful in completing this challenge.

# Function Description

# Complete the levelOrder function in the editor below.

# levelOrder has the following parameter:
# - Node pointer root: a reference to the root of the tree

# Prints
# - Print node.data items as space-separated line of integers. No return value is expected.

# Input Format

# The locked stub code in your editor reads the following inputs and assembles them into a BST:
# The first line contains an integer,  (the number of test cases).
# The  subsequent lines each contain an integer, , denoting the value of an element that must be added to the BST.

# Constraints



# Output Format

# Print the  value of each node in the tree's level-order traversal as a single line of  space-separated integers.

# Sample Input

# 6
# 3
# 5
# 4
# 7
# 2
# 1
# Sample Output

# 3 2 5 1 4 7 
# Explanation

# The input forms the following binary search tree:
# BST.png

# We traverse each level of the tree from the root downward, and we process the nodes at each level from left to right. The resulting level-order traversal is , and we print these data values as a single line of space-separated integers.

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        Q = []
        if (root.data is not None):
            Q.append(root)
        answer = ""
        while (Q):
            current = Q[0]
            answer = answer + str(current.data) + " "
            if current.left is not None:
                Q.append(current.left)
            if current.right is not None:
                Q.append(current.right)
            Q.pop(0)
        print(answer)
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)