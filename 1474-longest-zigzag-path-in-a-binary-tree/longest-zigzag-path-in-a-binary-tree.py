# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node, goLeft, length):
            if not node:
                return
            
            # update global answer
            self.ans = max(self.ans, length)
            
            if goLeft:
                # continue zigzag by going left
                dfs(node.left, False, length + 1)
                # restart zigzag by going right
                dfs(node.right, True, 1)
            else:
                # continue zigzag by going right
                dfs(node.right, True, length + 1)
                # restart zigzag by going left
                dfs(node.left, False, 1)
        
        dfs(root, True, 0)   # pretend we came from right
        dfs(root, False, 0)  # pretend we came from left
        
        return self.ans
