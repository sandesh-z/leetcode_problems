"""
Given the root of a binary tree, invert the tree, and return its root.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root   
       




s = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left= TreeNode(6)
root.right.right = TreeNode(9)

print(s.invertTree(root))