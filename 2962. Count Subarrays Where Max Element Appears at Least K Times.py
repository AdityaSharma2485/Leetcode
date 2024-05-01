class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_element = max(nums)
        left = 0
        count = 0
        subarrays_count = 0
        
        for right in range(n):
            if nums[right] == max_element:
                count += 1
            
            while count >= k:
                subarrays_count += n - right
                if nums[left] == max_element:
                    count -= 1
                left += 1
        
        return subarrays_count
