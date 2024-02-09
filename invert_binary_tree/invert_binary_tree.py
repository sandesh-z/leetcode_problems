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

        if root and root.left and root.right:
            
            root.left,root.right = root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)

        elif(root and root.left and not root.right):
            root.left,root.right = None,root.left
            self.invertTree(root.left)  
        elif(root and root.right and not root.left):
            root.left,root.right = root.right,None
            self.invertTree(root.right)     
            
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