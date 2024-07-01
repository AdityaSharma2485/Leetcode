# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Helper function to perform in-order traversal
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        # Helper function to build balanced BST from sorted list
        def build_balanced_bst(sorted_nodes):
            if not sorted_nodes:
                return None
            mid = len(sorted_nodes) // 2
            root = TreeNode(sorted_nodes[mid])
            root.left = build_balanced_bst(sorted_nodes[:mid])
            root.right = build_balanced_bst(sorted_nodes[mid+1:])
            return root
        
        # Get the sorted nodes via in-order traversal
        sorted_nodes = inorder_traversal(root)
        
        # Build and return the balanced BST
        return build_balanced_bst(sorted_nodes)
