"""
Given the root of a binary tree,
check whether it is a mirror of itself (i.e., symmetric around its center).
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        elif(p.val!=q.val):
            return False
        else:
            return True and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) 
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        left = self.invertTree(root.left)
        right = root.right

        return self.isSameTree(left,right)




       

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right =TreeNode(4)
root.right.left= TreeNode(4)
root.right.right= TreeNode(3)

print(s.isSymmetric(root))
