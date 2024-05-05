class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Traverse to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Pop the top node from the stack
            current = stack.pop()
            # Process the current node
            result.append(current.val)
            # Move to the right child
            current = current.right
        
        return result
