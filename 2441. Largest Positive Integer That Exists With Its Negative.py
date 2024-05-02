class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        for i in sorted(set(nums), reverse= True):
            if -i in nums:
                return i
        else:
            return -1
