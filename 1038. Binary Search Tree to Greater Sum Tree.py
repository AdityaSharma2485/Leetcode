# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def reverse_in_order_traversal(node, acc_sum):
            if not node:
                return acc_sum
            # Traverse right subtree first
            acc_sum = reverse_in_order_traversal(node.right, acc_sum)
            # Update node value
            node.val += acc_sum
            # Update accumulated sum
            acc_sum = node.val
            # Traverse left subtree
            return reverse_in_order_traversal(node.left, acc_sum)

        reverse_in_order_traversal(root, 0)
        return root

# Helper function to print the tree in level order
def print_level_order(root):
    if not root:
        return []
    
    from collections import deque
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.popleft()
            if node:
                level_nodes.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level_nodes.append(None)
        result.append(level_nodes)
    
    # Remove trailing Nones
    while result and result[-1] == [None] * len(result[-1]):
        result.pop()
    
    return result
