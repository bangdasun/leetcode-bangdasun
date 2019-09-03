# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        output = []
        if root is None:
            return output
        
        queue.append(root)
        
        while len(queue) > 0:
            level_output = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node is not None:
                    level_output.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            output.append(level_output)
        
        return output


from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque([root])
        output = []
        
        while len(queue) > 0:
            level_output = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_output.append(node.val)            
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            output.append(level_output)
        
        return output
