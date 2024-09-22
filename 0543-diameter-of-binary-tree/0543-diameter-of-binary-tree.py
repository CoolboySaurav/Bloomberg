# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = float("-inf")
        
        def helper(node):
            if not node:
                return -1
            
            left = helper(node.left)
            right = helper(node.right)
            
            self.diameter = max(self.diameter, (left + right + 2))
            
            return 1 + max(left, right)
        helper(root)
        
        return self.diameter
        
        
        
        