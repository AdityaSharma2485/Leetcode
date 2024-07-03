class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0  # If there are 4 or fewer elements, we can make all elements the same in at most 3 moves.
        
        nums.sort()
        
        # We consider the following scenarios:
        # 1. Remove the 3 largest elements
        # 2. Remove the 2 largest elements and 1 smallest element
        # 3. Remove the 1 largest element and 2 smallest elements
        # 4. Remove the 3 smallest elements
        
        return min(
            nums[-1] - nums[3],  # Remove the 3 smallest elements
            nums[-2] - nums[2],  # Remove the 2 smallest elements and 1 largest element
            nums[-3] - nums[1],  # Remove the 1 smallest element and 2 largest elements
            nums[-4] - nums[0]   # Remove the 3 largest elements
        )
