class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        # Initialize the answer variable with a dummy string value that is higher than any other valid strings
        smallest_string = '{'  # '{' is the character immediately after 'z' in ASCII

        def dfs(node, path):
            nonlocal smallest_string
            if node:
                # Convert current node's value to corresponding lowercase letter and prepend to path
                path.append(chr(ord('a') + node.val))
              
                # Check if current node is a leaf node (no children)
                if node.left is None and node.right is None:
                    # Create string from leaf to root and update smallest_string if necessary
                    current_string = ''.join(reversed(path))
                    smallest_string = min(smallest_string, current_string)
              
                # Continue depth-first search in left and right subtrees
                dfs(node.left, path)
                dfs(node.right, path)

                # Backtrack: remove the current node's character from path
                path.pop()

        # Start depth-first search from the root node
        dfs(root, [])
        return smallest_string
