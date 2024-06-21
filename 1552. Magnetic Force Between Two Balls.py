class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def canPlaceBalls(min_force):
            # Place the first ball at the first position
            count, last_position = 1, position[0]
            for pos in position[1:]:
                if pos - last_position >= min_force:
                    count += 1
                    last_position = pos
                if count == m:
                    return True
            return False
        
        # Sort the positions first
        position.sort()
        
        # Initialize binary search bounds
        left, right = 1, position[-1] - position[0]
        
        # Binary search for the largest minimum force
        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right
