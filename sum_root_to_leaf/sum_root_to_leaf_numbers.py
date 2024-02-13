"""
 You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #code generated with chat gpt
        def dfs(node:TreeNode, current_sum:int):
            if not node:
                return 0

            # Update the current sum
            current_sum = current_sum * 10 + node.val

            # If the current node is a leaf, return the current sum
            if not node.left and not node.right:
                return current_sum

            # Otherwise, continue DFS traversal
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        return dfs(root,0)


   
s = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left= TreeNode(6)
root.right.right = TreeNode(9)        

print(s.sumNumbers(root))
