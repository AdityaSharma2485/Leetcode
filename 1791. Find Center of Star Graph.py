class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # The center node must be one of the nodes in the first edge
        node1, node2 = edges[0]
        
        # Check if either node1 or node2 is the center by seeing if it appears in the second edge
        if node1 in edges[1]:
            return node1
        else:
            return node2
