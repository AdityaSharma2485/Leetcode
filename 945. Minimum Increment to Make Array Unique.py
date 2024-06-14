class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()
        
        # Initialize the number of moves needed
        moves = 0
        
        # Traverse the sorted array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is not greater than the previous one
            if nums[i] <= nums[i - 1]:
                # Calculate the necessary increment to make nums[i] unique
                increment = nums[i - 1] + 1 - nums[i]
                # Increment the current element
                nums[i] += increment
                # Add the number of increments to the total moves
                moves += increment
        
        return moves
