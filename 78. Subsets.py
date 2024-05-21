class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start, path):
            # Append the current subset to the result list
            result.append(path.copy())
            
            # Try to include each element starting from 'start' to the end of the list
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                path.append(nums[i])
                
                # Move to the next element
                backtrack(i + 1, path)
                
                # Exclude nums[i] from the current subset (backtrack)
                path.pop()
        
        # Start the backtracking with an empty path
        backtrack(0, [])
        
        return result
