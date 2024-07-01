from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        max_d = deque()  # stores the indices of the maximum elements
        min_d = deque()  # stores the indices of the minimum elements
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            # Maintain the max deque
            while max_d and nums[max_d[-1]] <= nums[right]:
                max_d.pop()
            max_d.append(right)
            
            # Maintain the min deque
            while min_d and nums[min_d[-1]] >= nums[right]:
                min_d.pop()
            min_d.append(right)
            
            # Ensure the window is valid
            while nums[max_d[0]] - nums[min_d[0]] > limit:
                left += 1
                # Remove elements not within the current window from the deques
                if max_d[0] < left:
                    max_d.popleft()
                if min_d[0] < left:
                    min_d.popleft()
            
            # Update the max length of the window
            max_len = max(max_len, right - left + 1)
        
        return max_len
