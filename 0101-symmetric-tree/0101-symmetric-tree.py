# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root):
        
        def isMirror(left, right):
            # Both nodes are null
            if not left and not right:
                return True
            
            # One is null or values differ
            if not left or not right or left.val != right.val:
                return False
            
            # Compare opposite children
            return (isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))
        
        return isMirror(root.left, root.right)