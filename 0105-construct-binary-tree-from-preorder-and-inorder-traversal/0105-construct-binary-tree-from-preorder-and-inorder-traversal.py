# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        indexMap = defaultdict(int)
        
        for i, node in enumerate(inorder):
            indexMap[node] = i
        
        
        def helper(preStart, preEnd, inStart, inEnd):
            if preStart > preEnd or inStart > inEnd:
                return None
            
            # Root is the first element in the preorder traversal
            root_val = preorder[preStart]
            root = TreeNode(root_val)
            
            # Get the index of the root in the inorder list
            index = indexMap[root_val]
            
            # Number of elements in the left subtree
            left_size = index - inStart
            
            # Recursively build left and right subtrees
            root.left = helper(preStart + 1, preStart + left_size, inStart, index - 1)
            root.right = helper(preStart + left_size + 1, preEnd, index + 1, inEnd)
            return root
        
        return helper(0, len(preorder) - 1, 0, len(inorder))