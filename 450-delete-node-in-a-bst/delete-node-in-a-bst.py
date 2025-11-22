class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        # search for key
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # node found
            # case 1: no left child
            if not root.left:
                return root.right
            
            # case 2: no right child
            if not root.right:
                return root.left
            
            # case 3: two children → find inorder successor
            successor = root.right
            while successor.left:
                successor = successor.left
            
            # replace value
            root.val = successor.val
            
            # delete successor from right subtree
            root.right = self.deleteNode(root.right, successor.val)
        
        return root
