class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        max_local = []
        
        for i in range(n - 2):
            max_local_row = []
            for j in range(n - 2):
                max_value = float('-inf')  # Initialize max_value to negative infinity
                for k in range(3):
                    for l in range(3):
                        max_value = max(max_value, grid[i + k][j + l])
                max_local_row.append(max_value)
            max_local.append(max_local_row)
        
        return max_local
