"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        sum = root.val
        if root:
            if not root.left and not root.right:
                if sum==targetSum:
                    return True
                return False
            if root.left:
                sum+=root.left.val
                res = self.hasPathSum(root.left,targetSum-root.val)
                if res:
                    return True
            if root.right:
                sum+=root.right.val
                res = self.hasPathSum(root.right,targetSum-root.val)   
                if res:
                    return True 
        return False         
            
            
    
s = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left= TreeNode(6)
root.right.right = TreeNode(9)
print(s.hasPathSum(root,17))    
