from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Use Counter to count occurrences of elements in nums1
        count = Counter(nums1)
        result = []

        # Iterate through nums2 and collect the intersection elements
        for num in nums2:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result
