class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Traverse the tree following BST rules
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        
        return None
