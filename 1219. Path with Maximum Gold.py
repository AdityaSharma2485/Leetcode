class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0 or visited[row][col]:
                return 0
            
            visited[row][col] = True
            current_gold = grid[row][col]
            max_gold = 0
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                max_gold = max(max_gold, dfs(new_row, new_col))
            
            visited[row][col] = False  # Backtrack
            return current_gold + max_gold
        
        m, n = len(grid), len(grid[0])
        max_gold_collected = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    visited = [[False] * n for _ in range(m)]
                    max_gold_collected = max(max_gold_collected, dfs(i, j))
        
        return max_gold_collected
