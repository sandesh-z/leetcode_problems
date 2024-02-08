# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        elif(p.val!=q.val):
            return False
        else:
            return True and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)        
        
        
    


s=Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.left.left = TreeNode(20)

print(s.isSameTree(root,root2))