from collections import Counter
from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        num_count = Counter(nums)
        sorted_keys = sorted(num_count.keys())
        
        for num in sorted_keys:
            while num_count[num] > 0:
                for i in range(k):
                    if num_count[num + i] > 0:
                        num_count[num + i] -= 1
                    else:
                        return False
        return True
