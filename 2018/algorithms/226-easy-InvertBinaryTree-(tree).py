# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return root
        
        temp_node = root.left
        root.left = root.right
        root.right = temp_node
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root
        