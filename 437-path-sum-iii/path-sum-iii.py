# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = {0: 1}   # prefix sum frequency map
        
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            
            # Count paths ending here with required sum
            count = prefix.get(curr_sum - targetSum, 0)
            
            # Add current prefix sum
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            
            # Continue to children
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            # Remove this prefix before going back up (backtracking)
            prefix[curr_sum] -= 1
            
            return count
        
        return dfs(root, 0)
