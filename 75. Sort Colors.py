class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Count occurrences of each color
        count = {0: 0, 1: 0, 2: 0}
        
        for num in nums:
            count[num] += 1
        
        # Overwrite the original list based on counts
        index = 0
        for color in range(3):  # Since we know the colors are 0, 1, and 2
            for _ in range(count[color]):
                nums[index] = color
                index += 1
